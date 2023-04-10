from .settings import *                  # settings.py(本番環境用)をimport

try:
    from .local import *      # local.py(開発環境用)をimport
except:
    pass