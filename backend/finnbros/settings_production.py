# Inherit from standard settings file for default
from selectboxsite.settings import *
import dj_database_url

# Everything below will override our standard settings:

# Parse database configuration from $DATABASE_URL

# db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Set debug to False
DEBUG = True
