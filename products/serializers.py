# products/serializers.py

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']

    # Custom validation for the price
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value

    # Custom validation for the stock
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be a negative number.")
        return value
