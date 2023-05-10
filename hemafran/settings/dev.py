from hemafran.settings.base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Email config
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
# EMAIL_HOST = env('EMAIL_HOST')
# EMAIL_PORT = env.int('EMAIL_PORT')
# EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', '')
# EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', '')
# EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=False)

INSTALLED_APPS += [
    # 3th apps
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# DEBUG TOOLBAR
INTERNAL_IPS = [
    'localhost',
    '127.0.0.1',
]
