from google.cloud import bigquery
from google.cloud import storage


    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset('my_new_dataset')

    job_config = bigquery.LoadJobConfig()
    schema = [
        bigquery.SchemaField('Years', 'STRING', mode='REQUIRED'),
        bigquery.SchemaField('Salary', 'STRING', mode='REQUIRED'),
    ]
    job_config.schema = schema
    job_config.skip_leading_rows = 1

    load_job = bigquery_client.load_table_from_uri(
        'gs://akanksha_bucket_1/Salary_Data.csv',
         dataset_ref.table('Salary_1'),job_config=job_config)

    assert load_job.job_type == 'load'

    load_job.result()  # Waits for table load to complete.

    assert load_job.state == 'DONE'


bq_load_csv_in_gcs()


