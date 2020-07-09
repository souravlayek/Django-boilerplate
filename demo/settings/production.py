from .base import *

DEBUG = False
ALLOWED_HOSTS = ['ip-adddress', 'www.your-domain.com']

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgress_db_name',
        'USER': 'dB username',
        'PASSWORD': 'db password',
        'HOST': 'localhost',
        'PORT':''
    }
}