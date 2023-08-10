from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import  APIView
from django.core.cache import cache

from apps.products.serializers import ProductSerializer
from apps.products.models import Product
from apps.products.utils import get_excel_response


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.select_related('category_id').prefetch_related("tags").all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        key = 'product_list'
        cached_data = cache.get(key)

        if cached_data is None:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            cache.set(key, serializer.data)
            return Response(serializer.data)

        return Response(cached_data)


class ProductExcelAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        response = get_excel_response()
        return response
