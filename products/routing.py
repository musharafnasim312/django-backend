from django.urls import path
from .consumers import ProductConsumer

websocket_urlpatterns = [
    path('ws/products/', ProductConsumer.as_asgi()),  # Use as_asgi() for async consumers
]