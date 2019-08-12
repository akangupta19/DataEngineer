from google.cloud import bigquery


def bq_load_csv_in_gcs():
    client = bigquery.Client()
    dataset_ref = client.dataset('my_new_dataset')
    table_ref = dataset_ref.table('Salary')

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1
    job_config.autodetect = True
    filename = 'gs://akanksha_bucket_1/Salary_Data.csv'


with open(filename, "rb") as source_file:
      job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

      job.result()  # Waits for table load to complete.

   print("Loaded {} rows into {}:{}.".format(job.output_rows, 'my_new_dataset', 'Salary' ))
