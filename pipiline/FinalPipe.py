from google.cloud import bigquery
import pandas as pd
import apache_beam as beam
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, StandardOptions

from apache_beam.io.gcp.internal.clients import bigquery

options = PipelineOptions()
google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'serene-vehicle-247610'
google_cloud_options.job_name = 'testingjob'
google_cloud_options.staging_location = 'gs://akanksha_bucket_1/staging'
google_cloud_options.temp_location = 'gs://akanksha_bucket_1/temp'
options.view_as(StandardOptions).runner = 'DataflowRunner'

table_spec = bigquery.TableReference(
        projectId='serene-vehicle-247610',
        datasetId='my_new_dataset',
        tableId='Prediction_Salaray')

table_schema = {'fields': [

    {'name': 'Years', 'type': 'STRING', 'mode': 'REQUIRED'},
    { 'name': 'Salary', 'type': 'STRING', 'mode': 'REQUIRED'},

]}


def GetMLDone(data):
    data = data[1]
    df = pd.DataFrame(data, columns=('YearsExperience', 'Salary'))
    df = df.iloc[1:, :]
    x = df[['YearsExperience']].values
    y = df[['Salary']].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
    regresor = LinearRegression()
    regresor.fit(x_train, y_train)
    pred = regresor.predict(x_test)
    # return pred

    thisdic = {}
    xlist = list(x_train)
    ylist = list(pred)
    l1 = []
    i = 0
    # temp=''
    for xval in xlist:
        for yval in ylist:
            temp = {}
    try:
        temp['Years'] = str(xval[0])
        temp['Salary'] = str(yval[0])
        l1.append(temp)
    except Exception:
        temp['Years'] = ' '
        temp['Salary'] = ' '
        l1.append(temp)
        print(l1)
        return(l1)
def printer(m):
   print(m)


p = beam.Pipeline('Directrunner')

lines=\
        (p | "ReadFromFile" >> beam.io.ReadFromText('gs://akanksha_bucket_1/Salary_Data.csv')


           |'Map record to key' >> beam.Map(lambda record: ('Data', record))
           | 'GroupBy data' >> beam.GroupByKey()
           # | "print data" >> beam.ParDo(printdata)
           | 'Build Model' >> beam.ParDo(GetMLDone)
            # | 'Build Model' >> beam.ParDo(export_items_to_bigquery)
           # | 'Combine' >> beam.CombineValues(beam.combiners.Dict)
           #| 'Write output to file' >> beam.io.WriteToText('gs://akanksha_bucket_1/SalaryOut.csv')

           |beam.io.WriteToBigQuery(
            table_spec,
            schema=table_schema,
            write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
            )

        )


p.run()