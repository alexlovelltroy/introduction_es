# -*- coding: utf-8 -*-

import os
from .base import *

DEBUG = True
# INSTALLED_APPS = list(INSTALLED_APPS) + ['devserver']

# Django-SES
#EMAIL_BACKEND = 'django_ses.SESBackend'
# These are optional -- if they're set as environment variables they won't
# need to be set here as well
# Override these here if you need to.  The defaults are loaded in base.py
#AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", False)
#AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", False)
#AWS_SES_REGION_NAME = os.environ.get("AWS_SES_REGION_NAME", "us-east-1")
#AWS_SES_REGION_ENDPOINT = os.environ.get("AWS_SES_REGION_ENDPOINT", "email.%s.amazonaws.com" % AWS_SES_REGION_NAME)

#AWS_ACCESS_KEY_ID = 'YOUR-ACCESS-KEY-ID'
#AWS_SECRET_ACCESS_KEY = 'YOUR-SECRET-ACCESS-KEY'
# Additionally, you can specify an optional region, like so:
AWS_SES_REGION_NAME = 'us-east-1'
AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'

# Django Storages S3
#AWS_ACCESS_KEY_ID
#AWS_SECRET_ACCESS_KEY
#AWS_STORAGE_BUCKET_NAME
#AWS_CALLING_FORMAT
AWS_HEADERS = {
    'Cache-Control': 'max-age=86400',
}

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATICFILES_STORAGE = 'django.core.files.storage.FileSystemStorage'
ALLOWED_HOSTS = ["127.0.0.1","localhost"]

# For database settings, the environment value with key "DATABASE_URL" will override all the settings.
#MYSQL
# the format for url: mysql://USERNAME:PASSWORD@HOST:PORT/DB_NAME
# the default:
# HOST: localhost
# PORT: 3306
# USER: introduction_es
# PASSWORD: introduction_es
# DB: introduction_es
# Uncomment this line for override the setings with mysql.
#DATABASES = {'default': dj_database_url.config(default='mysql://introduction_es:introduction_es@localhost:3306/introduction_es')}

#POSTGRES
# the format for url: postgres://USERNAME:PASSWORD@HOST:PORT/DB_NAME
# the default:
# HOST: localhost
# PORT: 5432
# USER: introduction_es
# PASSWORD: introduction_es
# DB: introduction_es
# Uncomment this line for override the setings with mysql.
#DATABASES = {'default': dj_database_url.config(default='postgres://introduction_es:introduction_es@localhost:5432/introduction_es')}


# add key based on https://developers.google.com/api-client-library/python/guide/aaa_oauth
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
#SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['https://mail.google.com']

try:
    from .local import *
except ImportError:
    pass
