from .settings import *

DEBUG = True
ALLOWED_HOSTS = []

SECRET_KEY = 'ixb62ha#ts=ab4t2u%p1_62-!5w2j==j6d^3-j$!z(@*m+-h'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path.joinpath(BASE_DIR, 'db.sqlite3'),
    }
}
