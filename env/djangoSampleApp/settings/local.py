from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

#INSTALLED_APPS += [
#    'debug_toolbar',
#]
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "static"),
#)

DATABASES = {
    'default': {
   #     'ENGINE': 'django.db.backends.sqlite3',
   #     'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',#追加
        'NAME': 'mkmkdb',  #追加 db名
        'USER': 'root',#追加
        'PASSWORD': '3349',#追加
       # 'HOST': '127.0.0.1',#追加
        'HOST': 'localhost',#追加       
        'PORT': '3306',#追加
    }
}

INTERNAL_IPS = ['127.0.0.1']