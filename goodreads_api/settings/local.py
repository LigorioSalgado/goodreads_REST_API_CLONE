from .base import * 

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'good_db',
       'USER': 'admin_good',
       'PASSWORD':'good2017',
       'HOST':'localhost',
       'PORT':'5432'
   }
}