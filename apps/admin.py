from django.contrib import admin
from .models import MyUser, Product

admin.site.register(MyUser)
admin.site.register(Product)