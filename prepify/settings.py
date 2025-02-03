import os
from dotenv import load_dotenv

load_dotenv()
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['157.245.123.144', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'tests',
    'admin_panel',
    # 'jazzmin',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'drf_yasg',
]

# JAZZMIN_SETTINGS = {
#     "site_title": "Prepify Admin",  # Заголовок страницы админки
#     "site_header": "Prepify Administration",  # Заголовок в шапке
#     "site_brand": "Prepify",  # Название бренда
#     "login_logo": None,
#     "site_logo": "images/logo.webp",  # Путь к логотипу (добавьте логотип в директорию static)
#     "welcome_sign": "Добро пожаловать в админку Prepify",  # Приветствие на главной странице админки
#     "copyright": "Prepify © 2024",  # Копирайт внизу страницы
#     "search_model": ["auth.User", "auth.Group"],  # Поиск по моделям
#     "custom_css": "css/main.css",

#     # Настройки навигации
#     "topmenu_links": [
#         {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},  # Ссылка на главную страницу админки
#         {"model": "auth.User"},  # Ссылка на пользователей
#         {"app": "your_app"},  # Ссылка на ваше приложение
#     ],

#     # Настройка бокового меню
#     "show_sidebar": True,  # Отображение бокового меню
#     "navigation_expanded": True,  # Меню развернуто по умолчанию
#     "hide_apps": [],  # Приложения, которые скрыты
#     "hide_models": [],  # Модели, которые скрыты
#     "order_with_respect_to": ["auth", "your_app"],  # Порядок отображения приложений
#     "icons": {
#         "auth": "fas fa-users-cog",
#         "auth.user": "fas fa-user",
#         "auth.Group": "fas fa-users",
#         "your_app.ModelName": "fas fa-layer-group",  # Пример настройки иконки для модели
#     },
    
#     # Дополнительные настройки
#     "show_ui_builder": False,  # Скрыть кнопку настройки интерфейса (рекомендуется оставить False в продакшене)
    
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prepify.urls'


CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",    
    "http://157.245.123.144:8085/"
]

CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"]
CORS_ALLOW_HEADERS = ["*"]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'prepify.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Prod
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': 'admin',
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# DEV
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": "mydatabase",
#     }
# }


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/'

# Каталог для хранения собранных статических файлов (после выполнения collectstatic)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Каталог для исходных статических файлов (которые вы создаете в процессе разработки)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Исходные статические файлы
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
