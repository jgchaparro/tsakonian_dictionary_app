"""
WSGI config for TsakonianDict project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Commenting out the following line used in complex method via GitHub:
# settings_module = "TsakonianDict.deployment" if 'WEBSITE_HOSTNAME' in os.environ else 'TsakonianDict.settings'

# Using simple method without GitHub:
settings_module = "TsakonianDict.settings"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()