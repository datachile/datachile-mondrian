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

###############################################
# BEGIN HACK TO SUPPORT CUSTOM AGGREGATORS
# Adapted from: http://jira.pentaho.com/browse/MONDRIAN-570?focusedCommentId=253824&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-253824
java_import 'mondrian.rolap.RolapAggregator'

class NoneRolapAggregator < Java::MondrianRolap::RolapAggregator

  def initialize(index)
    super('None', index, false)
  end

  java_signature 'public mondrian.olap.Aggregator getRollup()'
  def getRollup
    return self
  end

  java_signature 'public java.lang.Object aggregate(mondrian.olap.Evaluator, mondrian.calc.TupleList, mondrian.calc.Calc)'
  def aggregate(evaluator, members, exp)
    evaluator2 = evaluator.pushAggregation(members)
    evaluator2.setNonEmpty(false)
    return evaluator2.evaluateCurrent()
  end

  java_signature 'public java.lang.String getExpression(java.lang.String)'
  def getExpression(operand)
    return operand
  end

  java_signature 'public boolean supportsFastAggregates(mondrian.spi.Dialect.Datatype)'
  def supportsFastAggregates(dataType)
    return false
  end

end

enum = Java::mondrian.rolap.RolapAggregator.enumeration
index = enum.getMax
# reset field 'ordinalToValueMap' in order to make enumeration mutable again
ev = Java::JavaClass.for_name("mondrian.olap.EnumeratedValues")
f = ev.declared_field('ordinalToValueMap')
f.accessible = true
f.set_value(enum, nil)

enum.register(NoneRolapAggregator.new(index+1))
# END HACK
###############################################

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
