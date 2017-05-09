import os
from willblog.settings.common import *

DEBUG = False

SESSION_COOKIE_HTTPONLY = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'willtunner.me', 'www.willtunner.me']
ADMINS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'database/prod.sqlite3'),
    }
}
