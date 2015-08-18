from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + os.getenv('DB_TYPE', 'sqlite3'),
        'NAME': os.getenv('DB_NAME', 'challengeboard.db'),
        'USER': os.getenv('DB_USER', ''),
        'PASSWORD': os.getenv('DB_PASS', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', '')
    }
}

ALLOWED_HOSTS = [os.getenv('HOSTNAME', 'mrmcd.net')]

DEBUG = False
TEMPLATE_DEBUG = False

STATIC_ROOT = '/static/'
STATIC_URL = os.getenv('STATIC_URL', '/static/')

SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_DOMAIN = os.getenv('COOKIE_DOMAIN', '.mrmcd.net')
SESSION_COOKIE_SECURE = os.getenv('COOKIE_HTTPS', 'True') == 'True'
SESSION_COOKIE_NAME = os.getenv('COOKIE_PREFIX', '') + 'sessionid'

SECRET_KEY = os.getenv('SECRET', 'IVlaIt7M0z3W8yHH0NL1QYaPdzPOwW')

CSRF_COOKIE_DOMAIN = os.getenv('COOKIE_DOMAIN', '.mrmcd.net')
CSRF_COOKIE_NAME = os.getenv('COOKIE_PREFIX', '') + 'csrftoken'

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)