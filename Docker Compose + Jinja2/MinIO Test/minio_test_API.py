import boto3
from botocore.client import Config

# Configurazione MinIO locale
s3 = boto3.client('s3',
                  endpoint_url='http://localhost:9000',
                  aws_access_key_id='minioadmin',
                  aws_secret_access_key='minioadmin',
                  config=Config(signature_version='s3v4'),
                  region_name='us-east-1')

bucket_name = 'test-bucket'

# 1 -> Creare un bucket
s3.create_bucket(Bucket=bucket_name)

# 2 -> Caricare un file - si crea un file di esempio
file_name = 'esempio.txt'
with open(file_name, 'w') as f:
    f.write("Prova creazione file tramite API con MinIO")

# Caricamento del file sul bucket MinIO
s3.upload_file(file_name, bucket_name, file_name)
print(f"-> File '{file_name}' caricato con successo nel bucket '{bucket_name}'.")

# 3 -> Ottenere un URL temporaneo per accedere al file caricato
url = s3.generate_presigned_url('get_object',
                                Params={'Bucket': bucket_name, 'Key': file_name},
                                ExpiresIn=3600)

print("-> URL temporaneo per accedere al file caricato (valido 1 ora):")
print(url)
