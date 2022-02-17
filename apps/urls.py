from django.urls import path
from apps.views import UserCreateView, ProductCreateView

urlpatterns = [
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('create_product/', ProductCreateView.as_view(), name='product_create'),
    ]