#!/bin/bash

ALIAS="local"
BUCKET="test-bucket"
FILE="testfile2.txt"

echo "==> Crea file locale"
echo "Test creazione file il $(date)" > $FILE

echo "==> Carica file nel bucket: $BUCKET"
mc cp $FILE $ALIAS/$BUCKET/ # chiamata HTTP PUT verso endpoint http://localhost:9000/test-bucket/testfile2.txt

echo "==> Lista contenuto del bucket"
mc ls $ALIAS/$BUCKET/ # richiesta GET a http://localhost:9000/test-bucket e riceve in XML elenco oggetti

echo "==> Scarica file"
mc cp $ALIAS/$BUCKET/$FILE downloaded.txt # chiamata HTTP GET verso http://localhost:9000/test-bucket/testfile2.txt

echo "==> Contenuto scaricato:"
cat downloaded.txt


# mc é il MinIO Client, che permette di interagire con MinIO e altri servizi compatibili con S3 API.
# Pensato per interfacciarsi con MinIO, AWS S3 e altri object storage compatibili con S3 API.