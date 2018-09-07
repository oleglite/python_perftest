import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8al^v$8hc*2bhib51gm)m_)e**fc&@%yh&f^z0mobre^)im_8q'

DEBUG = False

ALLOWED_HOSTS = ['localhost']


INSTALLED_APPS = [
    'django.contrib.contenttypes',

    'mysite',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:' if os.environ.get('IN_MEMORY_DB') else 'db.sqlite3',
    }
}
LOGGING = None
