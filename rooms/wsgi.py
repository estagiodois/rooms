"""
WSGI config for rooms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application

get_wsgi_application.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rooms.settings')

application = get_wsgi_application()
