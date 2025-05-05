# ApplicationSystem/settings
"""
Django的配置文件（重要）
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# 获取当前目录的绝对路�?
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '39lpa05#hgfg0b01)b*xs-rlg8&6*x^w8&4wi8va%)=axo6h4m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['139.155.248.15']
# ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.management',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',

    # 以下为我们创建的应用
    'Api.testapp',
    'Api.apply',
    'Api.students',
    'Api.auth',
    'Api.filter',
    'Api.setting',
    'Api.field',
    'Api.percent',
    'Api.files',
    'Api.interview',
    'Api.date',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = "ApplicationSystem.urls"

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = ['http://localhost:5173']
CORS_ALLOWED_ORIGINS = ['http://localhost:5173']
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-applicant-id',
]

# 静态文件 URL 前缀
STATIC_URL = '/static/'

# 设置静态文件的目录，设置为列表形式
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # 添加模板目录路径
        ],
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

WSGI_APPLICATION = 'ApplicationSystem.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引�?
        'NAME': 'palm_apply',  # 数据库名�?
        'HOST': '127.0.0.1',  # 数据库地址，本�?虚拟) ip 地址 127.0.0.1
        'PORT': 3306,  # 端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456',  # 数据库密码

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 设置默认的主键字段类型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 静态文件根路径
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# 图片储存根路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 图片访问URL
MEDIA_URL = '/media/'
