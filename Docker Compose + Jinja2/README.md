# MinIO 
> Official Documentation -> https://min.io/docs/minio/kubernetes/upstream/

## Access files
## [SDK](https://min.io/docs/minio/linux/developers/minio-drivers.html)

MinIO ha pubblicato tra i SDK (Go, java, .NET, JavScript, Haskell, C++, Rust):

### [Python](https://min.io/docs/minio/linux/developers/minio-drivers.html#python-sdk)

- [Quickstart Guide](https://min.io/docs/minio/linux/developers/python/minio-py.html)

#### Install Methods:
```bash
pip3 install minio
```
- Source
```bash
git clone https://github.com/minio/minio-py
cd minio-py
python setup.py install
```

### [File Uploader](https://min.io/docs/minio/linux/developers/python/minio-py.html)
```python
# file_uploader.py MinIO Python SDK example
from minio import Minio
from minio.error import S3Error

def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio("play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

    # The file to upload, change this path if needed
    source_file = "/tmp/test-file.txt"

    # The destination bucket and filename on the MinIO server
    bucket_name = "python-test-bucket"
    destination_file = "my-test-file.txt"

    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # Upload the file, renaming it in the process
    client.fput_object(
        bucket_name, destination_file, source_file,
    )
#    print(
        source_file, "successfully uploaded as object",
        destination_file, "to bucket", bucket_name,
    )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
```
## [Client "mc"](https://min.io/docs/minio/linux/reference/minio-mc.html?ref=docs)
### Install
#### 64-bit Intel
```bash
curl https://dl.min.io/client/mc/release/linux-amd64/mc \
  --create-dirs \
  -o $HOME/minio-binaries/mc

chmod +x $HOME/minio-binaries/mc
export PATH=$PATH:$HOME/minio-binaries/

mc --help
```

### Create an Alias for the S3-Compatible Service
Use the _**mc alias set**_ command to add an Amazon S3-compatible service to the mc configuration.

```bash
bash +o history
mc alias set ALIAS HOSTNAME ACCESS_KEY SECRET_KEY
bash -o history
```
- Replace ALIAS with a name to associate to the S3 service. mc commands typically require ALIAS as an argument for identifying which S3 service to execute against.
- Replace HOSTNAME with the URL endpoint or IP address of the S3 service.
- Replace ACCESS_KEY and SECRET_KEY with the access and secret keys for a user on the S3 service.

Replace each argument with the required values. If you omit the ACCESS_KEY and SECRET_KEY, the command prompts you to enter those values in the CLI.

Each of the following tabs contains a provider-specific example:
### Add an Alias for a [MinIO deployment](https://min.io/docs/minio/linux/reference/minio-mc/mc-alias-set.html)

```bash
mc alias set $ALIAS $ENDPOINT $ACCESS_KEY $SECRET_KEY
```

### Test the connection

```bash
mc admin info myminio
```

### Download a file from MinIO using "mc" client

```bash
mc cp $ALIAS/$BUCKET/$REMOTE_FILE $LOCAL_DEST
```

### [MinIO Server](https://min.io/docs/minio/linux/reference/minio-server/minio-server.html)

```
minio server /mnt/disk{1...4}
```

_______________________________________

Variabili








