import os
from willblog.settings.common import *

DEBUG = False

SESSION_COOKIE_HTTPONLY = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ] # add your hosts
ADMINS = () # add your admins

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/web/tmp/django_cache',
        'TIMEOUT': 21600, # cache passed 3h
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

# change your database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'database/prod.sqlite3'),
    }
}
