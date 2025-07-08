import boto3
import requests
from botocore.client import Config

# Configurazione MinIO locale
s3 = boto3.client('s3',
                  endpoint_url='http://localhost:9000',
                  aws_access_key_id='minioadmin',
                  aws_secret_access_key='minioadmin',
                  config=Config(signature_version='s3v4'),
                  region_name='us-east-1')

bucket_name = 'test-bucket-url'

# Crea il bucket se non esiste già
try:
    s3.create_bucket(Bucket=bucket_name)
except s3.exceptions.BucketAlreadyOwnedByYou:
    print(f"Bucket '{bucket_name}' già esistente!")

# URL pubblico del file da scaricare
file_url = 'https://via.placeholder.com/150'  # esempio immagine pubblica
file_name = 'immagine_scaricata.png'

# Scarica il file dall'URL
response = requests.get(file_url)

if response.status_code == 200:
    # Carica direttamente il file su MinIO
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=response.content)
    print(f"-> File '{file_name}' scaricato da URL e caricato nel bucket '{bucket_name}'.")

    # Genera URL temporaneo (opzionale)
    url = s3.generate_presigned_url('get_object',
                                    Params={'Bucket': bucket_name, 'Key': file_name},
                                    ExpiresIn=3600)
    print("-> URL temporaneo per visualizzare il file (valido 1 ora):")
    print(url)
else:
    print(f"Errore nel download del file: {response.status_code}")
