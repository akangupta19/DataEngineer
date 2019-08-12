from google.cloud import bigquery
import pandas as pd
import apache_beam as beam
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, StandardOptions

from apache_beam.io.gcp.internal.clients import bigquery

from apache_beam.internal import pickler
from apache_beam.pvalue import PCollection
from apache_beam.runners import create_runner
from apache_beam.runners import PipelineRunner
from apache_beam.transforms import ptransform
from apache_beam.typehints import typehints
from apache_beam.typehints import TypeCheckError
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.options.pipeline_options import StandardOptions
from apache_beam.options.pipeline_options import TypeOptions
from apache_beam.options.pipeline_options_validator import PipelineOptionsValidator

table_spec = bigquery.TableReference(
        projectId='serene-vehicle-247610',
        datasetId='my_new_dataset',
        tableId='Prediction_Salaray')



table_schema = {'fields': [
{'name': 'Years', 'type': 'STRING', 'mode': 'REQUIRED'},
{'name': 'Salary', 'type': 'STRING', 'mode': 'REQUIRED'}
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
                temp['Salary']=str(yval[0])
                l1.append(temp)
            except Exception:
                 temp['Years']=' '
                 temp['Salary']=' '
                 l1.append(temp)
    print(type(l1))
    return(l1)
def printer(m):
   print(m)

p = beam.Pipeline('Directrunner')
lines=(p
| 'ReadMyFile' >> beam.io.ReadFromText('gs://akanksha_bucket_1/Salary_Data.csv')
| 'Splitter using beam.Map' >> beam.Map(lambda record: (record.split(',')))
| 'Map record to 1' >> beam.Map(lambda record: ('M', record))
| 'GroupBy the data' >> beam.GroupByKey()
| 'Get the prediction' >> beam.ParDo(GetMLDone)
| beam.io.WriteToBigQuery(
table_spec,schema=table_schema,
write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED)


       )
p.run()



