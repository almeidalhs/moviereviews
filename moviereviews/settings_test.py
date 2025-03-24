from .settings import *

DEBUG = False
TESTING = True  # Custom flag to indicate test mode

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",  # Speed up password hashing
]

# shutdown staticfiles
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# local memcache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"  # Prevent actual emails from being sent
