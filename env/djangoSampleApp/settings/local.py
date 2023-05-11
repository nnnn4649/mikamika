from .base import *


#テスト用

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ['127.0.0.1']


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',#追加
        'NAME': 'mkmkdb',  #追加 db名
        'USER': 'root',#追加
        'PASSWORD': '3349',#追加
        'HOST': '127.0.0.1',#追加
        'HOST': 'localhost',#追加       
        'PORT': '3306',#追加
    }
}

#本番用

#DEBUG = False

#ALLOWED_HOSTS = ["mikamika.tk"]

#DATABASES = { 
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'mkdb',
#        'USER': 'root',
#        'PASSWORD': '0<w<r?FHaFql123',
#        'HOST': 'localhost',
#        'PORT': '3306',
#    }
#}