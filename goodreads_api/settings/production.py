from .base import *
DEBUG = False

ALLOWED_HOSTS = ['*']


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'good_db',
       'USER': 'good_admin',
       'PASSWORD':'good2017',
       'HOST':'localhost',
       'PORT':'5432'
   }
}