from google.cloud import bigquery
from google.oauth2.credentials import Credentials

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_bigquery(data, **kwargs):

    credentials_path = "/home/src/application_default_credentials.json"

    credentials = Credentials.from_authorized_user_file(
        credentials_path
    )

    client = bigquery.Client(
        credentials=credentials,
        project='uber-project-493612'
    )

    dataset_id = "uber_DE"

    for table_name, df in data.items():

        table_id = f"uber-project-493612.{dataset_id}.{table_name}"

        job = client.load_table_from_dataframe(
            df,
            table_id
        )

        job.result()

        print(f"Loaded {job.output_rows} rows into {table_id}")