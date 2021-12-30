from django.contrib import admin
from .models import Product, Category, Tag, CartItem, Order

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(CartItem)
admin.site.register(Order)