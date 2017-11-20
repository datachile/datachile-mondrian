require 'json'
require 'nokogiri'

SCHEMA = Nokogiri::XML(STDIN.read)

cubes = SCHEMA.xpath("//Cube")

o = cubes.reduce({}) { |memo, cube|
  source_name = cube.xpath("./Annotations/Annotation[@name='source_name']").text.strip
  source_link = cube.xpath("./Annotations/Annotation[@name='source_link']").text.strip

  if !(source_name.empty? or source_link.empty?)
    memo[cube.attribute('name').value] = {
      'title' => source_name,
      'url' => source_link
    }
  end

  memo
}
puts JSON.pretty_generate(o)

