from datetime import timedelta
from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['*']

CUSTOM_APP = [
    'todo_app'
]

INSTALLED_LIBRARIES = [
    'rest_framework',
    'drf_spectacular',
]

INSTALLED_APPS = [
                     'django.contrib.admin',
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                 ] + CUSTOM_APP + INSTALLED_LIBRARIES

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": config('DB_ENGINE', cast=str),
        "NAME": config('DB_NAME', cast=str),
        "USER": config('DB_USER', cast=str),
        "PASSWORD": config('DB_PASSWORD', cast=str),
        "HOST": config('DB_HOST', cast=str),
        "PORT": config('DB_PORT', cast=int),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Directory where collected static files will be stored
STATIC_ROOT = BASE_DIR / 'static/collect_static'

# Additional directories to look for static files during development
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'TODO',
    'DESCRIPTION': 'Django project',
    'VERSION': '1.0.0',
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
        'docExpansion': 'none',
        # To prevent schema to be appeared uncomment the following
        # 'defaultModelsExpandDepth': -1,
    },
    'DEFAULT_AUTO_SCHEMA': 'drf_spectacular.openapi.AutoSchema',
    'SERVE_INCLUDE_SCHEMA': False,
    'SERVE_PUBLIC': True,
    'USE_SESSION_AUTH': False,
    'REDUCER': 'drf_spectacular.reducing.RouterDepthReducer',
    'COMPONENT_SPLIT_REQUEST': True,

    "SWAGGER_UI_DIST": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest",
    "SWAGGER_UI_FAVICON_HREF": STATIC_URL + "images/api.ico",

    'DEFAULT_FIELD_INSPECTORS': [
        'drf_spectacular.inspectors.CamelCaseJSONFilter',
        'drf_spectacular.inspectors.InlineSerializerInspector',
        'drf_spectacular.inspectors.RelatedFieldInspector',
        'drf_spectacular.inspectors.ChoiceFieldInspector',
        'drf_spectacular.inspectors.FileFieldInspector',
        'drf_spectacular.inspectors.DictFieldInspector',
        'drf_spectacular.inspectors.SimpleFieldInspector',
        'drf_spectacular.inspectors.StringDefaultFieldInspector',
    ],

}
