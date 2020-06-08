from website.core.settings.defaults import *

ALLOWED_HOSTS = [
    'jpnerdbio.com',
    'www.jpnerdbio.com',
]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_STORAGE_BUCKET_NAME = 'cdn.jpnerdbio.com'

AWS_S3_REGION_NAME = 'us-west-2'

AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME
