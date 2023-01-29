import os 
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'serviceKey.json'

storage_client = storage.Client()
"""
bucket_name = 'bucket_firt'
bucket = storage_client.bucket(bucket_name)
bucket.location = 'US'
bucket = storage_client.create_bucket(bucket)
"""