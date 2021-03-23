from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '9x=57*mq51*$zry30untmkzi$wsafrfr60o97itz+o4m+t0!l0')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Herok
if os.getenv("HEROKU_DEPLOY", ""):
    try:
        import dj_database_url
        ALLOWED_HOSTS = ["localhost", "127.0.0.1", "mysterious-meadow-14996.herokuapp.com"] 
        DATABASE_URL = os.environ.get('DATABASE_URL')
        db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
        DATABASES['default'].update(db_from_env)
    except Exception as e:
        raise Exception(e)

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "mysterious-meadow-14996.herokuapp.com"] 

# Flower
# flower -a project --port 5555 --broker=redis://:foobared@127.0.0.1:6379

# Celery
# redis://:password@hostname:port/db_number
CELERY_BROKER_URL = os.getenv('CELERY_BROKER', "redis://:foobared@127.0.0.1:6379/0")
# os.setenv("CELERY_BROKER", CELERY_BROKER)
CELERY_RESULT_BACKEND = os.getenv('CELERY_BACKEND', "redis://:foobared@127.0.0.1:6379/0")
# os.setenv("CELERY_BACKEND", CELERY_BACKEND)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'flask_forge.apps.FlaskForgeConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'project', 'templates') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'project', 'static')
]

