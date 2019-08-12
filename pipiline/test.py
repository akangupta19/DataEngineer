import apache_beam as beam


p = beam.Pipeline('Directrunner')

lines = \
      (p | "readfromfile" >> beam.io.ReadFromText('a.txt')
        | "firsttreamfoirm" >> beam.FlatMap(lambda word: [len(word)])
         | "outpuile" >> beam.io.WriteToText('c.txt')
    )
p.run()



p = beam.Pipeline('Directrunner')
data_from_source = (p
| 'ReadMyFile' >> beam.io.ReadFromText('gs://akanksha_bucket_1/Salary_Data.csv')
| 'Splitter using beam.Map' >> beam.Map(lambda record: (record.split(',')))
| 'Map record to 1' >> beam.Map(lambda record: ('M', record))
| 'GroupBy the data' >> beam.GroupByKey()
| 'Get the prediction' >> beam.ParDo(GetMLDone)
| beam.io.WriteToBigQuery(
schema=table_schema,
table="serene-vehicle-247610.my_new_dataset.Prediction_Salaray",
write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED)
)

p.run()