from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import permission_required

urlpatterns = [
	path('', permission_required('is_staff')(views.IndexView.as_view()), name = "dashboard-index"),
	path('order/details/<int:pk>/', permission_required('is_staff')(views.OrderDetailView.as_view()), name = "order-details"),
	path('product/create', permission_required('is_staff')(views.ProductCreateView.as_view()), name = "create-product"),
	path('products/', permission_required('is_staff')(views.ProductListView.as_view()), name = "product-list"),
	path('product/edit/<int:pk>/', permission_required('is_staff')(views.ProductEditView.as_view()), name = "product-edit"),
	path('orders/pending/', permission_required('is_staff')(views.PendingOrdersView.as_view()), name = "pending-orders"),
]