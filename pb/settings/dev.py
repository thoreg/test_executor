from pb.settings.base import *

SECRET_KEY = 'abc5mr8&koa!t!!&t39%o5*i^al)402_k%uk)@r+*3du(&0e1#'

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.db'),
    }
}

BROKER_URL = 'redis://localhost:6379/0'
