from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create a product
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# List and filter products (GET with pagination and filtering)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['name', 'price']  # Enable filtering

# Retrieve, Update, Delete a specific product
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        if 'stock' in serializer.validated_data:
            self.notify_stock_update(instance)

    def notify_stock_update(self, product):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "product_notifications", {
                "type": "send_product_notification",
                "message": {
                    "product_id": product.id,
                    "name": product.name,
                    "stock": product.stock
                }
            }
        )
