from django.conf import settings
settings.configure()

import django 
django.setup()

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from website.consumer import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pollution.settings")

application = get_asgi_application()

ws_patterns = [
    path('ws/test/', TestConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'websocket' : URLRouter(ws_patterns)
})
