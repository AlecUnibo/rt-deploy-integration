from jinja2 import Environment, FileSystemLoader
import os

# Directory dove si trova il template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('docker-compose.yml.j2')

# Variabili da sostituire nel template
context = {
    'container_name': 'minio-local-compose',
    'api_port': 9000,
    'console_port': 9001,
    'minio_user': 'minioadmin',
    'minio_password': 'minioadmin',
    'volume_name': 'minio_data',
    'minio_domain': 'minio.localhost'
}

# Render e salvataggio del file finale
rendered = template.render(context)

with open('docker-compose.yml', 'w') as f:
    f.write(rendered)

print("-> docker-compose.yml generato con successo")
