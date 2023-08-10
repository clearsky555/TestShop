from rest_framework import serializers

from apps.products.models import Product
from apps.users.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

