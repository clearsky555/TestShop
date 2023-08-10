from django.shortcuts import render


from rest_framework.generics import CreateAPIView
from rest_framework.permissions import  AllowAny
from rest_framework.response import Response
from apps.users.serializers import CreateUserSerializer
# Create your views here.


class CreateUserAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        message = "User registered successfully"
        return Response(data={"message":message, "data":response.data})