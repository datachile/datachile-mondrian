require 'sinatra'
require 'sequel'
require 'logger'

CREATE_SEARCH_TABLE_QUERY = <<-Q
create schema if not exists search;

CREATE EXTENSION if not exists unaccent;

DROP TEXT SEARCH CONFIGURATION IF EXISTS es CASCADE;
CREATE TEXT SEARCH CONFIGURATION es ( COPY = spanish );
ALTER TEXT SEARCH CONFIGURATION es ALTER MAPPING
FOR hword, hword_part, word WITH unaccent, spanish_stem;

DROP TEXT SEARCH CONFIGURATION IF EXISTS en CASCADE;
CREATE TEXT SEARCH CONFIGURATION en ( COPY = english );
ALTER TEXT SEARCH CONFIGURATION en ALTER MAPPING
FOR hword, hword_part, word WITH unaccent, english_stem;

create table if not exists search.search_index
(
	id serial not null,
	content text,
  index_as text,
	member_data jsonb not null,
	language text not null,
	cube text not null,
	dimension text not null,
	hierarchy text not null,
	level text not null,
	key text not null,
	depth integer not null,
	constraint search_index_language_cube_dimension_hierarchy_level_key_depth
		primary key (language, cube, dimension, hierarchy, level, key, depth)
);

CREATE INDEX IF NOT EXISTS es_search_index_idx ON search.search_index 
USING gin(to_tsvector('es', content))
WHERE language = 'es';

Q

module Mondrian::REST
  module Search
    class SearchController < Sinatra::Base

      CPARAM = db_connection(ENV['MONDRIAN_REST_CONF'])
      SEARCH_INDEX_TABLE = Sequel[:search][:search_index]

      DB = Sequel.connect("jdbc:postgresql://#{CPARAM[:host]}:#{CPARAM[:port]}/#{CPARAM[:database]}?user=#{CPARAM[:username]}&password=#{CPARAM[:password]}")
      DB.extension :pg_json
      DB.loggers << Logger.new(STDERR)

      DB.run CREATE_SEARCH_TABLE_QUERY

      DEFAULT_LANGUAGE = 'en'
      DEFAULT_SEARCH_LIMIT = 20

      get '/' do
        q, limit, offset, lang = params.values_at('q', 'limit', 'offset', 'lang')
        limit ||= DEFAULT_SEARCH_LIMIT
        lang ||= DEFAULT_LANGUAGE

        # SELECT "content", "index_as" FROM "search"."search_index" WHERE (to_tsvector(CAST('es' AS regconfig), (COALESCE("content", ''))) @@ plainto_tsquery(CAST('es' AS regconfig), 'animal')) ORDER BY ts_rank_cd(to_tsvector(CAST('es' AS regconfig), (COALESCE("content", ''))), plainto_tsquery(CAST('es' AS regconfig), 'animal')) DESC

        DB[SEARCH_INDEX_TABLE]
          .full_text_search(
            :content,
            q,
            :language => lang,
            :plain => true,
            :rank => true
          )
          .select(
            :content,
            :key,
            :index_as,
            Sequel.lit("(CASE WHEN DEPTH > 1 THEN member_data->'ancestors'->0->'key' ELSE NULL END) AS ancestor_key"),
            Sequel.lit("(CASE WHEN DEPTH > 1 THEN member_data->'ancestors'->0->'name' ELSE NULL END) AS ancestor_name"))
          .limit(limit)
          .to_a
          .to_json
      end

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
            .insert_conflict(constraint: 'search_index_language_cube_dimension_hierarchy_level_key_depth',
                             update: {
                               content: Sequel[:excluded][:content],
                               member_data: Sequel[:excluded][:member_data]
                             }) # upsert
            .multi_insert(
              @members.map { |member|
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
                  depth: member['depth']
                }
              }
            )
        end
        201 # created
      end
    end
  end
end
