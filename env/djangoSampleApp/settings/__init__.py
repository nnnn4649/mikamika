from .settings import *                  # settings.py(本番環境用)をimport

#mport pymysql #追記

#pymysql.install_as_MySQLdb() #追記

try:
    from .local import *      # local.py(開発環境用)をimport
except:
    pass