import os

from website.core.settings.defaults import *


ALLOWED_HOSTS = [
    'jpnerdbio.com',
    'www.jpnerdbio.com',
]

DEBUG = False

#guid generator but better to use random string like:
# >>> import string import random
# >>> ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(96)])
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'cdn.jpnerdbio.com'
# AWS_S3_REGION_NAME = 'us-west-2'
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'