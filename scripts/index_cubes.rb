#!/usr/bin/env ruby
require "uri"
require "json"
require "logger"

require "slop"
require "rest-client"

LOG = Logger.new(STDERR)

opts = Slop.parse do |o|
  o.string '-m', '--mondrian-endpoint', 'URL for mondrian-rest server', required: true
  o.string '-f', '--fts-endpoint', 'URL for FTS server'
  o.string '-l', '--default-language', 'Default language', required: true
  o.bool '-d', '--dry-run', 'Print indexable objects to STDERR instead of indexing them', default: false
  o.array '-i', '--include', 'Only index the specified index_as declarations', default: []
end

OPTS = opts.to_hash

if OPTS[:dry_run] && OPTS[:fts_endpoint]
  STDERR.puts "-d and -f are mutually exclusive"
  STDERR.puts opts
  exit 1
end

if !OPTS[:dry_run] && OPTS[:fts_endpoint].nil?
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
    .find_all { |d| d['annotations'].has_key?('index_as') && (OPTS[:include].empty? ? true : OPTS[:include].include?(d['annotations']['index_as'])) } \
    .reduce({}) { |memo, d| memo[d['annotations']['index_as']] = d; memo }
end

def indexable_objects(idx_dimension)
  Enumerator.new do |enum|
    idx_dimension['hierarchies'].each do |h|
      h['levels'].shift if h['has_all'] # skip indexing of "All" member
      h['levels'].each_with_index do |level, level_depth|

        min_depth = idx_dimension.dig('annotations', 'index_min_depth')
        min_depth = min_depth.nil? ? 0 : min_depth.to_i
        if min_depth > level_depth + 1
          LOG.info "Skipping level #{level_depth}"
          next
        end

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
              depth: level['depth'] - (min_depth - 1)
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
            depth: level['depth'] - (min_depth - 1)
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
      enum.yield dim, indexable_objects(dim).to_a.flatten
    end
  end
end

index_cube_objects(OPTS[:mondrian_endpoint],
                   OPTS[:default_language]).each { |dim, members|

  next if members.empty?

  LOG.info "Indexing #{members.size} elements"
  if OPTS[:fts_endpoint]
    LOG.info URI.join(OPTS[:fts_endpoint], "index_objects").to_s
    RestClient.post(URI.join(OPTS[:fts_endpoint], "index_objects").to_s,
                    members.to_json,
                    :content_type => :json,
                    :accept => :json)

  elsif OPTS[:dry_run]
    puts members.to_json
  end
  #puts
}

