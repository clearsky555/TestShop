from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="TestShop API",
        default_version='v1',
        description="TestShop",
        contact=openapi.Contact(email="admin@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


from apps.products import views as p_views
from apps.users import views as user_views

urlpatterns = [
    path('docs/', schema_view.with_ui("swagger")),
    path('products/', p_views.ProductListAPIView.as_view()),
    path('products/export/', p_views.ProductExcelAPIView.as_view()),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', user_views.CreateUserAPIView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]