from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-c8t*cc%#t9a)stiade^&j47n&sw&x1_0r5!^+_fgg6ll15%92&'

#DEBUG = False

#ALLOWED_HOSTS = ["mikamika.tk"]

AUTH_USER_MODEL = 'accounts.CustomUser'# 追加

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mikamika', 
    'bootstrap4',
    'accounts', # 追加
    'django.contrib.sites', # 追加
    'allauth', # 追加
    'allauth.account', # 追加
    'allauth.socialaccount', # 追加
    'inquiries',#追加
    'djangoSampleApp',
    'channels', #追加
    'widget_tweaks'
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', #デフォルトの認証基盤
    'allauth.account.auth_backends.AuthenticationBackend' # メールアドレスとパスワードの両方を用いて認証するために必要
)

ACCOUNT_AUTHENTICATION_METHOD = 'email' # メールアドレス（とパスワードで）認証する
ACCOUNT_USERNAME_REQUIRED = True # サインアップ（ユーザー登録）の時にユーザーネームを尋ねる
ACCOUNT_EMAIL_REQUIRED = True # サインアップ（ユーザー登録）の時にメールアドレスを尋ねる
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' # メール検証を必須とする

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_URL = '/accounts/login/' # ログインURLの設定
LOGIN_REDIRECT_URL = '/index/' # ログイン後のリダイレクト先
ACCOUNT_LOGOUT_REDIRECT_URL = '/index/' #　ログアウト後のリダイレクト先


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoSampleApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'bootstrap4.templatetags.bootstrap4',
             ],
        },
    },
]   

WSGI_APPLICATION = 'djangoSampleApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

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


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ja-jp'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#追加

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #画像アップロード用追加
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Channels
ASGI_APPLICATION = 'djangoSampleApp.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': { 'hosts': [('127.0.0.1', 6379)], }, #127.0.0.1
    },
}
