#Como se tiene que configurar el archivo para pythonanywhere
import os
import sys

#path = os.path.expanduser('/home/username/mysitio')
path = "/home/username/mysitio"
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysitio.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
