require 'csv'
require 'nokogiri'

schema_path = ARGV.first

schema = File.open(schema_path) { |f| Nokogiri::XML(f) }

CSV.parse(STDIN, headers: true) do |row|
  it = schema.xpath("//InlineTable[@alias='#{row['table_name']}']")
  it_row = it.at_xpath("./Rows/Row/Value[@column='#{row['id_column_name']}' and text()='#{row['id_value']}']/parent::Row")
  if it_row.nil?
    STDERR.puts "Can't find <Row> for table #{row['table_name']} and id #{row['id_value']}"
    next
  end
  it_row.at_xpath(".//Value[@column='description']").content = row['description'].strip
  it_row.at_xpath(".//Value[@column='es_description']").content = row['es_description'].strip
end

STDOUT << schema.to_xml
