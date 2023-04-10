"""
WSGI config for djangoSampleApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys 

from django.core.wsgi import get_wsgi_application

#path = '/var/www/html/djangoSampleApp'

#if path not in sys.path:
 #   sys.path.append(path)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
#sys.path.append('/home/ec2-user/mikamika-1/env/djangoSampleApp')   #### 追加 ####
#sys.path.append('/home/ec2-user/mikamika-1/env/djangoSampleApp/wsgi.py')   #### 追加 ####
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoSampleApp.settings.local')

application = get_wsgi_application()
