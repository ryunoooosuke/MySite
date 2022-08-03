"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

load_dotenv('../.env')

envstate = os.getenv('ENV_STATE', 'local')
if envstate == 'production':
    # settings/production.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
else:
    # settings/local.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

application = get_wsgi_application()
