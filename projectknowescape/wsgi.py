"""
WSGI config for projectandromedes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectknowescape.settings')

application = get_wsgi_application()

try:
    call_command('apply_migrations')
except Exception as e:
    print(f"Error applying migrations: {e}")
# vercel prod variable
app = application
