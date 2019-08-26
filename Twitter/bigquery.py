from google.cloud import bigquery
from google.cloud import storage

def bq_create_dataset():
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset('my_new_dataset')

    try:
        bigquery_client.get_dataset(dataset_ref)
    except Exception:
        dataset = bigquery.Dataset(dataset_ref)
        dataset = bigquery_client.create_dataset(dataset)
        print('Dataset {} created.'.format(dataset.dataset_id))


#bq_create_dataset()


def bq_create_table():
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset('my_new_dataset')

    # Prepares a reference to the table
    table_ref = dataset_ref.table('twitter')

    try:
        bigquery_client.get_table(table_ref)
    except Exception:
        schema = [
            bigquery.SchemaField('Id', 'STRING', mode='REQUIRED'),
            bigquery.SchemaField('Tweet', 'STRING', mode='REQUIRED'),
            bigquery.SchemaField('Label', 'STRING', mode='REQUIRED'),
        ]
        table = bigquery.Table(table_ref, schema=schema)
        table = bigquery_client.create_table(table)
        print('table {} created.'.format(table.table_id))

bq_create_table()





