module Datachile
  class NamedQueries < Grape::API

    resource :queries do
      content_type :xls, "application/vnd.ms-excel"
      formatter :xls, Mondrian::REST::Formatters::XLS

      content_type :csv, "text/csv"
      formatter :csv, Mondrian::REST::Formatters::CSV

      content_type :json, "application/json"
      formatter :json, Mondrian::REST::Formatters::AggregationJSON

      content_type :jsonrecords, "application/x-jsonrecords"
      formatter :jsonrecords, Mondrian::REST::Formatters::JSONRecords

      # content_type :jsonstat, "application/x-jsonstat"
      # formatter :jsonstat, Mondrian::REST::Formatters::JSONStat


      get '/testquery' do
        m = <<MDX
SELECT NON EMPTY {[Measures].[FOB US]} ON COLUMNS,
NON EMPTY [Date].[Date].[Year].Members ON ROWS
FROM [exports]
MDX
        mdx(m)
      end

      get '/anothertestquery' do
        m = <<MDX
SELECT NON EMPTY {[Measures].[CIF US]} ON COLUMNS,
NON EMPTY [Date].[Date].[Year].Members ON ROWS
FROM [imports]
MDX
        mdx(m)
      end
    end
  end
end
