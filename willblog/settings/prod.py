import os
from willblog.settings.bases import *

DEBUG = False

SESSION_COOKIE_HTTPONLY = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
ADMINS = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'database/prod.sqlite3'),
    }
}

CACHE_PATH = os.path.dirname(os.path.join(os.path.dirname(BASE_DIR)))
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(CACHE_PATH, 'django_cache'),
        'TIMEOUT': 21600, # cache passed 3h
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_NAME = 'sd'
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = os.path.join(CACHE_PATH, 'django_session')
