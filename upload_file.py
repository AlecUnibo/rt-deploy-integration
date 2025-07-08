import boto3
from botocore.client import Config
import sys
import os

if len(sys.argv) != 2:
    print("Uso: python upload_file.py <percorso_file>")
    sys.exit(1)

file_path = sys.argv[1]
file_name = os.path.basename(file_path)
bucket_name = 'test-bucket'

# Connessione MinIO
s3 = boto3.client('s3',
    endpoint_url='https://{{ minio_domain }}',  # <-- dominio pubblico servito via Traefik
    aws_access_key_id='{{ minio_user }}',
    aws_secret_access_key='{{ minio_password }}',
    config=Config(signature_version='s3v4'),
    region_name='us-east-1')


# Creazione bucket (ignora errore se esiste)
try:
    s3.create_bucket(Bucket=bucket_name)
except s3.exceptions.BucketAlreadyOwnedByYou:
    pass

# Upload file
s3.upload_file(file_path, bucket_name, file_name)
print(f"File '{file_name}' caricato nel bucket '{bucket_name}'.")

# Genera URL temporaneo
url = s3.generate_presigned_url('get_object',
                                Params={'Bucket': bucket_name, 'Key': file_name},
                                ExpiresIn=3600)
print("URL temporaneo valido per 1 ora:")
print(url)
