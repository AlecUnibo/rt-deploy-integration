import boto3
from botocore.client import Config

# Configurazione client MinIO
s3 = boto3.client('s3',
                  endpoint_url='http://localhost:9000',
                  aws_access_key_id='minioadmin',
                  aws_secret_access_key='minioadmin',
                  config=Config(signature_version='s3v4'),
                  region_name='us-east-1')

bucket_name = 'test-bucket'
file_name = 'esempio.txt'          # Nome del file nel bucket
local_download = 'scaricato.txt'   # Nome del file scaricato localmente

# Scarica il file dal bucket e salvalo in locale
try:
    s3.download_file(bucket_name, file_name, local_download)
    print(f"-> File '{file_name}' scaricato correttamente come '{local_download}'")
except Exception as e:
    print(f"!X!X! Errore nel download: {e} !X!X!")
