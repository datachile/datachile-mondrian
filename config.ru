require 'bundler'
Bundler.setup

require 'rack/cors'
require 'rack/config'
require 'rack/deflater'

require 'jdbc/postgres'

Jdbc::Postgres.load_driver

require 'logger'
require 'mondrian_rest'

logger = Logger.new(STDERR)
logger.level = Logger::DEBUG

PARAMS = {
  driver: 'postgresql',
  host: 'hermes',
  port: 5432,
  database: 'datachile',
  username: 'datachile',
  password: 'yapoweon',
  catalog: File.join(File.dirname(__FILE__), 'schema.xml')
}

use Rack::Config do |env|
  env['mondrian-olap.params'] = PARAMS
end

run Mondrian::REST::Api
