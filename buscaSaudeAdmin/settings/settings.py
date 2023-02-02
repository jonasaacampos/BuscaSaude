from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-2x_@x*qh#ne=jnr%wqj7m+tswx$txf3hdzqs43w6+*=yo&zmdc"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "buscaSaude",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "buscaSaudeAdmin.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "buscaSaudeAdmin.wsgi.application"

############
# Database #
############
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

## Configurações removidas, será considerado o arquivo de cnexão individual (prod, test, dev, etc)
"""
PostgreSQL
(venv) tiago_luiz@ubuntu:~/livro_django$ pip install psycopg2
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.postgresql_psycopg2',
 'NAME': 'Nome do seu banco de dados',
 'USER': 'Nome do usuário',
 'PASSWORD': 'Senha',
 'HOST': 'Nome do host de conexão ao banco',
 'PORT': 'Número da porta de comunicação',
 }
}
MariaDB ou MySQL
(venv) tiago_luiz@ubuntu:~/livro_django$ pip install mysqlclient
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.mysql',
 'NAME': 'Nome do seu banco de dados',
 'USER': 'Nome do usuário',
 'PASSWORD': 'Senha',
 'HOST': 'Nome do host de conexão ao banco',
 'PORT': 'Número da porta de comunicação',
 }
}
SQLServer
(venv) tiago_luiz@ubuntu:~/livro_django$ pip install django-pyodbc-azure
DATABASES = {
 'default': {
 'ENGINE': 'sql_server.pyodbc',
 'NAME': 'Nome do seu banco de dados',
 'USER': 'Nome do usuário',
 'PASSWORD': 'Senha',
 'HOST': 'Nome do host de conexão ao banco',
 'PORT': 'Número da porta de comunicação',
 },
}
Oracle
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.oracle',
 'NAME': 'Nome do seu banco de dados',
 'USER': 'Nome do usuário',
 'PASSWORD': 'Senha',
 'HOST': '',
 'PORT': '',
 }
}
# Se você não usar um arquivo tnsnames.ora e for realizar a conexão usando
o SID, preencha o HOST e o PORT:
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.oracle',
 'NAME': 'Nome do seu banco de dados',
 'USER': 'Nome do usuário',
 'PASSWORD': 'Senha',
 'HOST': 'Nome do host de conexão ao banco',
 'PORT': 'Número da porta de comunicação',
 }
}
"""





# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = Path.joinpath(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
