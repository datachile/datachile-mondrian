#!/usr/bin/env ruby
require "uri"
require "json"
require "logger"

require "slop"
require "rest-client"

LOG = Logger.new(STDERR)

opts = Slop.parse do |o|
  o.string '-m', '--mondrian-endpoint', 'URL for mondrian-rest server'
  o.string '-f', '--fts-endpoint', 'URL for FTS server'
  o.string '-l', '--default-language', 'Default language'
end

OPTS = opts.to_hash
if OPTS[:mondrian_endpoint].nil?
  STDERR.puts "need -m option"
  STDERR.puts opts
  exit 1
end

if OPTS[:fts_endpoint].nil?
  STDERR.puts "need -f option"
  STDERR.puts opts
  exit 1
end

if OPTS[:default_language].nil?
  STDERR.puts "need -l option"
  STDERR.puts opts
  exit 1
end

##
# get all the dimensions annotated with 'index_as'
def indexable_dimensions(cubes)
  cubes \
    .flat_map { |c| c['dimensions'].each { |d| d[:cube_name] = c['name'] }; c['dimensions'] } \
    .find_all { |d| d['annotations'].has_key?('index_as') } \
    .reduce({}) { |memo, d| memo[d['annotations']['index_as']] = d; memo }
end

def indexable_objects(idx_dimension)
  Enumerator.new do |enum|
    idx_dimension['hierarchies'].each do |h|
      h['levels'].shift if h['has_all'] # skip indexing of "All" member
      h['levels'].each_with_index do |level, level_depth|

        max_depth = idx_dimension.dig('annotations', 'index_max_depth')
        max_depth = max_depth.nil? ? 100 : max_depth.to_i
        if max_depth <= level_depth
          LOG.info "Reached level depth #{level_depth}, skipping"
          break
        end


        # if there are localized properties defined in this level, get them from the server
        lprops = (level['annotations'] || {}).find_all { |k, v| k.end_with?('_caption') }.to_h

        params = { params: {
                     member_properties: lprops.values
                   }
                 } unless lprops.empty?

        r = JSON.parse(
          RestClient.get(
            URI.join(OPTS[:mondrian_endpoint],
                     "/cubes/#{idx_dimension[:cube_name]}/dimensions/#{URI.escape(idx_dimension['name'])}/levels/#{URI.escape(level['name'])}/members").to_s,
            params)
        )

        enum.yield lprops.reduce([]) { |memo, (ann_k, ann_v)|
          lang, prop = ann_k.to_s.split('_')

          memo + r['members'].map { |member|
            {
              language: lang,
              content: member['properties'][ann_v],
              member_data: member,
              index_as: idx_dimension['annotations']['index_as'],
              cube: idx_dimension[:cube_name],
              dimension: idx_dimension['name'],
              hierarchy: h['name'],
              level: level['name'],
              key: member['key'],
              depth: level['depth']
            }
          }
        }

        # always index members in the default language
        enum.yield r['members'].map { |member|
          {
            language: OPTS[:default_language],
            content: member['caption'],
            member_data: member,
            index_as: idx_dimension['annotations']['index_as'],
            cube: idx_dimension[:cube_name],
            dimension: idx_dimension['name'],
            hierarchy: h['name'],
            level: level['name'],
            key: member['key'],
            depth: level['depth']
          }
        }
      end
    end
  end
end


def index_cube_objects(mondrian_endpoint, default_language)

  defined_cubes = JSON.parse(
    RestClient.get(
      URI.join(mondrian_endpoint, 'cubes').to_s
    ))['cubes']

  idx_dims = indexable_dimensions(defined_cubes)

  Enumerator.new do |enum|
    idx_dims.each do |index_as, dim|
      enum.yield indexable_objects(dim).to_a.flatten
    end
  end
end

index_cube_objects(OPTS[:mondrian_endpoint],
                   OPTS[:default_language]).each { |members|

  next if members.empty?

  LOG.info "Indexing #{members.size} elements"
  LOG.info URI.join(OPTS[:fts_endpoint], "index_objects").to_s
  RestClient.post(URI.join(OPTS[:fts_endpoint], "index_objects").to_s,
                  members.to_json,
                  :content_type => :json,
                  :accept => :json)

  #puts
}

