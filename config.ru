require 'yaml'

require 'jbundler'

require 'rack/cors'
require 'rack/config'
require 'jdbc/postgres'

Jdbc::Postgres.load_driver

require 'logger'
require 'mondrian_rest'

require_relative './lib/none_rolap_aggregator.rb'
require_relative './lib/named_queries.rb'
require_relative './lib/db_connection.rb'
require_relative './lib/search.rb'

logger = Logger.new(STDERR)
logger.level = Logger::DEBUG

PARAMS = db_connection(ENV['MONDRIAN_REST_CONF'])

use Rack::Config do |env|
  env['mondrian-olap.params'] = PARAMS
end

use Rack::Cors do
  allow do
    origins '*'
    resource '*', headers: :any, methods: :get
  end
end

Mondrian::REST::Api.mount Datachile::NamedQueries

app = Rack::Builder.new do
  map '/' do
    run Mondrian::REST::Api
  end

  map '/search' do
    run Mondrian::REST::Search::SearchController
  end
end

run app
