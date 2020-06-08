from website.core.settings.defaults import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(k+j6=zei=_^w!z*0(mkm94crl_knpl(86b(yalcv2#+trv+ro'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}