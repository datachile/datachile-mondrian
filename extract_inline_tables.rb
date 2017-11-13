require 'nokogiri'
require 'csv'

csv = CSV.instance
csv << ['table_name', 'id_column_name', 'id_value', 'description', 'es_description']

SCHEMA = Nokogiri::XML(STDIN.read)
inline_tables = SCHEMA.xpath("//InlineTable")

inline_tables.each do |it|
  table_name = it.attribute('alias').value
  id_column_name = it.xpath("./ColumnDefs/ColumnDef[contains(@name, 'id')]").first.attribute('name').value
  it.xpath('./Rows/Row').each do |row|
    csv << [table_name,
            id_column_name,
            row.xpath("./Value[@column='#{id_column_name}']").text.strip,
            row.xpath("./Value[@column='description']").text.strip,
            row.xpath("./Value[@column='es_description']").text.strip]
  end
end
