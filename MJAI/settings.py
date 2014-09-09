import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '$o--(@8r#^krx&1x205w@p@b*h81i267p%6abe)g^jn8=_u!z5'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Portfolio'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'MJAI.urls'
WSGI_APPLICATION = 'MJAI.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

UPLOADS = os.path.join(BASE_DIR, 'uploads')
MEDIA_ROOT = UPLOADS
MEDIA_URL = '/uploads/'

STATIC_URL = '/static/'

# Grappelli Stuff
GRAPPELLI_ADMIN_TITLE = 'MJ Art Inspiration'
