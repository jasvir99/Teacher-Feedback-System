import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'Teacher-Feedback-System.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
sys.path.append('mpath')

