import os
import sys


# set variables
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'resume_builder.settings'

import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
#application = PassengerPathInfoFix(application)
#application = WhiteNoise(application, root='/home/specsoah/public_html/hospital/public')
