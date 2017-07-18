require 'rack/cors'
require 'rack/config'
require 'jdbc/postgres'

Jdbc::Postgres.load_driver

require 'logger'
require 'mondrian_rest'

require_relative './lib/none_rolap_aggregator.rb'

logger = Logger.new(STDERR)
logger.level = Logger::DEBUG

PARAMS = if !ENV['MONDRIAN_REST_CONF'].nil? and File.exists? ENV['MONDRIAN_REST_CONF']
           require 'yaml'
           YAML.load_file(ENV['MONDRIAN_REST_CONF'])
         else
           {
             driver: 'postgresql',
             host: 'hermes',
             port: 5433,
             database: 'datachile',
             username: 'datachile',
             password: 'yapoweon',
             catalog: File.join(File.dirname(__FILE__), 'schema.xml')
           }
         end


use Rack::Config do |env|
  env['mondrian-olap.params'] = PARAMS
end

use Rack::Cors do
  allow do
    origins '*'
    resource '*', headers: :any, methods: :get
  end
end

use Rack::CommonLogger, $stdout
run Mondrian::REST::Api
