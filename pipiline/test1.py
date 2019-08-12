import pandas as pd
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
p = beam.Pipeline('Directrunner')
def printdata(value):
  print(value[1])

def slplt(value):
  value= (value.split(','))
  return value

def MLmodel(data):
   df = pd.DataFrame(data[1][1:], columns=('date', 'open', 'high','low', 'close', 'vol'))
   print(df.head(), df.info())


lines = \
(p | 'ReadFileFromCSV' >> beam.io.ReadFromText('Google_Stock_Price_Train.csv')
| 'Splitter using beam.Map' >> beam.Map(slplt)
| 'Map record to key' >> beam.Map(lambda record: ('MBA', record))
| 'GroupBy data' >> beam.GroupByKey()
# | "print data" >> beam.ParDo(printdata)
| 'Build Model' >> beam.ParDo(MLmodel)
# | 'Combine' >> beam.CombineValues(beam.combiners.Dict)
# | 'Write output to file' >> beam.io.WriteToText('StockMarketoutput.csv')
)
p.run()

