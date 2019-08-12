import argparse
import logging
import re

from past.builtins import unicode
from apache_beam.io.gcp.internal.clients import bigquery


import apache_beam as beam
from apache_beam.io import ReadFromText

from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, StandardOptions
from apache_beam.options.pipeline_options import SetupOptions




options = PipelineOptions()
google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'serene-vehicle-247610'
google_cloud_options.job_name = 'testingjob'
google_cloud_options.staging_location = 'gs://akanksha_bucket_1/staging'
google_cloud_options.temp_location = 'gs://akanksha_bucket_1/temp'
options.view_as(StandardOptions).runner = 'DataflowRunner'

table_schema = {'fields': [

    {'name': 'Years', 'type': 'STRING', 'mode': 'REQUIRED'},
    { 'name': 'Salary', 'type': 'STRING', 'mode': 'REQUIRED'},

]}


table_spec = bigquery.TableReference(
        projectId='serene-vehicle-247610',
        datasetId='my_new_dataset',
        tableId='Prediction_Salaray')


def MLmodel(data):
    dataset = pd.read_csv('Salary_Data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    pred=regressor.predict(X_test)
    print(pred)
    return pred

def export_items_to_bigquery():
     # Instantiates a client
    bigquery_client = bigquery.Client()

    # Prepares a reference to the dataset
    dataset_ref = bigquery_client.dataset('my_new_dataset')

    table_ref = dataset_ref.table('predic')
    table = bigquery_client.get_table(table_ref)  # API call

    rows_to_insert = [pred]
    errors = bigquery_client.insert_rows(table, rows_to_insert)  # API request
    assert errors == []



p = beam.Pipeline(options=options)

lines=\
        (p | "ReadFromFile" >> beam.io.ReadFromText('gs://akanksha_bucket_1/Salary_Data.csv')


           |'Map record to key' >> beam.Map(lambda record: ('Data', record))
           | 'GroupBy data' >> beam.GroupByKey()
           # | "print data" >> beam.ParDo(printdata)
           | 'Build Model' >> beam.ParDo(MLmodel)
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
