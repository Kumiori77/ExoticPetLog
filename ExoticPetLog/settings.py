"""
Django settings for ExoticPetLog project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from django.core.exceptions import ImproperlyConfigured


# 베포 위해추가
# 환경변수 받아오는 함수
def get_env_variable(var_name):
  try:
    return os.environ[var_name]
  except KeyError:
    error_msg = 'Set the {} environment variable'.format(var_name)
    raise ImproperlyConfigured(error_msg)



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 로컬 테스트용
# SECRET_KEY = my_settings.SECRET_KEY
# 베포용
SECRET_KEY = get_env_variable("DJANGO_SECRET")



# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True # 개발용
DEBUG = False # 베포용

ALLOWED_HOSTS = ["*"]


# 베포 위해 추가
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


# 베포 위해 추가 (csrf 방지)
CSRF_TRUSTED_ORIGINS =["https://port-0-exoticpetlog-ixj2mllkg7wiz.sel3.cloudtype.app"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'record',
    # 추가 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 베포 위해 추가
    'corsheaders',
]

MIDDLEWARE = [
    # 베포 위해 추가
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 베포 위해 추가
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'ExoticPetLog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 추가 (인증)
                 "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = 'ExoticPetLog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# 로컬 테스트 용
# DATABASES = my_settings.DATABASES
# 베포용
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': get_env_variable('DATABASE'), 
        'USER': get_env_variable('DB_USER'),                    
        'PASSWORD': get_env_variable('DB_PW'),        
        'HOST': get_env_variable('DB_HOST'),          
        'PORT': get_env_variable('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
# 베포 위해 추가 (static) 모으기
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 유저가 미디어 파일 업로드 위해 추가
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# 인증 위해 추가

AUTHENTICATION_BACKENDS = [   
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

AUTH_USER_MODEL = "record.User"

LOGIN_REDIRECT_URL = "/"



###########################################################################################################

# 로컬 테스트 세팅

# """
# Django settings for ExoticPetLog project.

# Generated by 'django-admin startproject' using Django 4.2.2.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.2/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/4.2/ref/settings/
# """

# from pathlib import Path
# import os
# # 로컬 테스트 용
# import my_settings 





# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# # 로컬 테스트용
# SECRET_KEY = my_settings.SECRET_KEY


# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True # 개발용


# ALLOWED_HOSTS = ["*"]



# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'record',
#     # 추가 
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
# ]

# MIDDLEWARE = [
#     # 베포 위해 추가
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     # 베포 위해 추가
#     'whitenoise.middleware.WhiteNoiseMiddleware',
# ]

# ROOT_URLCONF = 'ExoticPetLog.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, "templates")],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#                 # 추가 (인증)
#                  "django.template.context_processors.request",
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'ExoticPetLog.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# # 로컬 테스트 용
# DATABASES = my_settings.DATABASES



# # Password validation
# # https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     # {
#     #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     # },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     # {
#     #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     # },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = '/static/'
# # 베포 위해 추가 (static) 모으기
# STATIC_ROOT = os.path.join(BASE_DIR, "static")


# # 유저가 미디어 파일 업로드 위해 추가
# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# # Default primary key field type
# # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# # 인증 위해 추가

# AUTHENTICATION_BACKENDS = [   
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]

# SITE_ID = 1

# AUTH_USER_MODEL = "record.User"

# LOGIN_REDIRECT_URL = "/"

