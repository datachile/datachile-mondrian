require 'sinatra'
require 'sequel'
require 'logger'

CREATE_SEARCH_TABLE_QUERY = <<-Q
create schema if not exists search;

CREATE EXTENSION IF NOT EXISTS unaccent;
CREATE EXTENSION IF NOT EXISTS pg_trgm;

CREATE OR REPLACE FUNCTION f_unaccent(TEXT)
  RETURNS TEXT AS
$func$
SELECT unaccent('unaccent', $1)
$func$ LANGUAGE SQL IMMUTABLE SET search_path = public, pg_temp;

create table if not exists search.search_index
(
	id serial not null,
	content text,
	index_as text,
	member_data jsonb not null,
	language text not null,
	-- cube text not null,
	dimension text not null,
	hierarchy text not null,
	level text not null,
	key text not null,
	depth integer not null,
  multilanguage boolean not null,
	constraint search_index_language_dimension_hierarchy_level_key_depth_pk
		primary key (language, dimension, hierarchy, level, key, depth)
);


CREATE INDEX IF NOT EXISTS trgm_search_index ON search.search_index
USING gist (f_unaccent(content) gist_trgm_ops);
Q

SEARCH_QUERY = <<-SQL
 WITH search_query AS
 (SELECT
    si.content,
    si.member_data -> 'key'                          AS key,
    si."index_as",
    si.member_data -> 'name'                         AS "name",
    si.depth,
    si.language,
    (CASE WHEN si.DEPTH > 2
      THEN (si.member_data -> 'ancestors' -> 0 -> 'key')
     ELSE NULL END)                                  AS ancestor_key,
    si.multilanguage                                 AS multilanguage,
    similarity(f_unaccent(si.content), :q) AS sim
  FROM "search"."search_index" si
  WHERE ((CASE WHEN si.multilanguage
    THEN si.language = :lang
          ELSE si.language = '' END) AND (si.content IS NOT NULL) AND
         (si.index_as NOT IN ('institutions', 'careers')))
  ORDER BY similarity(f_unaccent(si.content), :q) DESC
  LIMIT :limit
  OFFSET :offset)

 SELECT
   sq.*,
   xi.content as ancestor_name
 FROM search_query sq
   LEFT OUTER JOIN search.search_index xi
     ON
       xi.depth = sq.depth - 1 AND sq.ancestor_key = (xi.member_data -> 'key') AND
       xi.index_as = sq.index_as AND sq.language = xi.language
 ORDER BY similarity(f_unaccent(sq.content), :q) DESC
SQL

module Mondrian::REST
  module Search
    class SearchController < Sinatra::Base

      CPARAM = db_connection(ENV['MONDRIAN_REST_CONF'])
      SEARCH_INDEX_TABLE = Sequel[:search][:search_index]

      DB = Sequel.connect("jdbc:postgresql://#{CPARAM[:host]}:#{CPARAM[:port]}/#{CPARAM[:database]}?user=#{CPARAM[:username]}&password=#{CPARAM[:password]}")
      DB.extension :pg_json
      DB.loggers << Logger.new(STDOUT)

      DB.run CREATE_SEARCH_TABLE_QUERY

      DB.run "SELECT set_limit(0.1)"

      DEFAULT_LANGUAGE = 'en'
      DEFAULT_SEARCH_LIMIT = 20

      get '/' do
        content_type :json, 'charset' => 'utf-8'

        q, limit, offset, lang = params.values_at('q', 'limit', 'offset', 'lang')
        limit ||= DEFAULT_SEARCH_LIMIT
        lang ||= DEFAULT_LANGUAGE
        offset ||= 0

        DB.fetch(SEARCH_QUERY,
                 q: q, limit: limit, offset: offset, lang: lang)
          .to_a
          .to_json
      end

      UNIQ_BY = ["language", "dimension", "hierarchy", "level", "key", "depth"]

      before do
        rb = request.body.read
        if rb.size > 0
          @members = JSON.parse(rb)
        end
      end
      post '/index_objects' do
        # XXX TODO protect with a secret token or something
        DB.transaction do
          DB[SEARCH_INDEX_TABLE]
            .insert_conflict(constraint: 'search_index_language_dimension_hierarchy_level_key_depth_pk',
                             update: {
                               content: Sequel[:excluded][:content],
                               member_data: Sequel[:excluded][:member_data]
                             }) # upsert
            .multi_insert(
              @members
                .uniq { |r| UNIQ_BY.map { |k| r[k] }.join('--') }
                .map { |member|
                {
                  language: member['language'],
                  content: member['content'],
                  index_as: member['index_as'],
                  member_data: Sequel.pg_json(member['member_data']),
                  cube: member['cube'],
                  dimension: member['dimension'],
                  hierarchy: member['hierarchy'],
                  level: member['level'],
                  key: member['key'],
                  depth: member['depth'],
                  multilanguage: member['multilanguage']
                }
              }
            )
        end
        201 # created
      end
    end
  end
end
