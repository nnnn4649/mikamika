from .base import *


#DEBUG = True
DEBUG = False

#ALLOWED_HOSTS = ['*']


#DATABASES = {
   # 'default': {
   #     'ENGINE': 'django.db.backends.sqlite3',
   #     'NAME': BASE_DIR / 'db.sqlite3',
   #     'ENGINE': 'django.db.backends.mysql',#追加
  #      'NAME': 'mkmkdb',  #追加 db名
   #     'USER': 'root',#追加
   #     'PASSWORD': '3349',#追加
       # 'HOST': '127.0.0.1',#追加
  #      'HOST': 'localhost',#追加       
  #      'PORT': '3306',#追加
 #   }
#}

DATABASES = {
    'default': {
   #     'ENGINE': 'django.db.backends.sqlite3',
   #     'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',#追加
        'NAME': 'mkdb',  #追加 db名
        'USER': 'root',#追加
        'PASSWORD': '0<w<r?FHaFql123',#追加
        'HOST': 'localhost',#追加
        'PORT': '3306',#追加
    }
}

#INTERNAL_IPS = ['127.0.0.1']
ALLOWED_HOSTS = ["mikamika.tk"]