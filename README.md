# MinIO + Traefik + Docker Compose + Jinja2
> Questo progetto configura un ambiente completo per eseguire MinIO in locale, esposto tramite Traefik con supporto a HTTPS e routing dinamico, il tutto orchestrato con Docker Compose e automatizzato con Jinja2

## Introduzione alle tecnologie
* __MinIO__ -> object storage compatibile con Amazon S3, utile per salvere file/bucket via API [documentazione -> https://min.io/docs/minio/container/index.html]
* __Traefik__ -> revers proxy moderno che rileva automaticamente i container e li esponde tramite dominio (es: https://minio.localhost) [documentazione -> https://traefik.io/traefik]
* __Docker Compose__ -> gestisce il tutto tramite file YAML [documentazione -> https://docs.docker.com/compose/]
* __Jinja2__ -> permette di automatizzare e templatizzare la configurazione in modo dinamico [documentazione -> https://jinja.palletsprojects.com/en/stable/]

## Come avviare l'ambiente
### A. Configurazione iniziale dell'ambiente
Installare python dal sito ufficiale __https://www.python.org/__ e creare successivamente un ambiente virtuale all'interno della directory del progetto

Da cmd o powershell, all'interno della directory, lanciare il seguente comando
```bash
python -m venv venv
```
E attivarlo con 

```bash
source venv/bin/activate
```
2. Installare poi i pacchetti richiesti:

Da cmd o powershell, lanciare il seguente comando
```bash
pip install jinja2 boto3
pip install requests
```

### B. Test per MinIO
Una volta preparato l'ambiente possiamo fare dei test per assicurarci del corretto funzionamento 

Creazione di Bucket e file tramite API
Da cmd o powershell, all'interno della directory "MinIO Test", lanciare il seguente comando
```bash
python minio_test_api.py
```

### C. Sviluppo dell'ambiente
#### 1. Generare il _docker-compose.yml_ tramite il template jinja2
Da cmd o powershell, all'interno della directory, lanciare il seguente comando
```bash
python render_compose.py
```
Variabili del *render_compose.py*, che andrá a creare il _docker-compose.yml_
- 'container_name': 'minio-local-compose',
- 'api_port': 9000,
- 'minio_user': 'minioadmin',
- 'minio_password': 'minioadmin',
- 'volume_name': 'minio_data',
- 'minio_domain': 'minio.localhost'

#### 2. Avviare Traefik
Da cmd o powershell, all'interno della directory, lanciare il seguente comando
```bash
docker compose -f docker-compose.traefik.yml up -d
```
#### 3. Avviare MinIO
Da cmd o powershell, all'interno della directory, lanciare il seguente comando
```bash
docker compose up -d
```
#### 4. Aggiungere al file hosts (se non é giá stato fatto)
```
127.0.0.1 minio.localhost
```
#### 5. Accedere ai servizi
* Per accedere all'interfaccia MinIO: __https://minio.localhost__

#### 6. Installa mc (MinIO Client)
Entrare in WSL, nel caso accedere se non é giá stato fatto e lanciare i seguenti comandi:
```bash
curl -O https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
sudo mv mc /usr/local/bin/
```
#### 7. Imposta l’alias local che corrisponde al server MinIO locale, autenticato.
```bash
mc alias set local http://localhost:9000 minioadmin minioadmin
```
E infine lancia:

```bash
./test_minio.sh
```

Accedere ai file:
- Tramite SDK -URL alla pagina- -URL a quickstart Python- (con supporto a diversi linguaggi - inserire esempio in Python) 
- Come ottenere file da SDK -URL- e metti esempio con Python
- Tramite Client tool "mc", come si installa, mettere architettura 64-bit Intel, come ci si autentica, MinIO Server esempio
- Come testare la connessione
- Come ottenere un file 








