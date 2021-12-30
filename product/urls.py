from django.urls import path
from . import views

# app_name = "product" 

urlpatterns = [
    path('', views.IndexView.as_view(), name = "index" ),
    path('home', views.IndexView.as_view(), name = "home" ),
    path('add-to-cart/', views.add_to_cart, name = "add_to_cart"),
    path('cart', views.CartView, name = "cart" ),
    path('product/showcase/<int:pk>/', views.ProductDetailView.as_view(), name="details"),
    path('refresh', views.RefreshNum, name = "refresh"),
    path('reduce', views.reduce_units, name = "reduce"),
]