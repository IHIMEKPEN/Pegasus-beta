from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from product.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

# Create your views here.
class IndexView(ListView):
	template_name = "dashboard/dashboard-index.html"
	model = Product
	paginate_by = 5

class OrderDetailView(UpdateView):
	model = Order
	fields = ['status']
	template_name = "dashboard/order-details.html"

	def get_success_url(self):
		return reverse('order-details', kwargs={'pk': self.object.id})

class ProductCreateView(CreateView):
	template_name = "forms.html"
	model = Product
	fields = ['image', 'name', 'description', 'price', 'available_units', 'category', 'tags']

	def get_success_url(self):
		return reverse('dashboard-index')

class ProductListView(ListView):
	template_name = "dashboard/productlist.html"

	def get_queryset(self):
		return Product.objects.all()

class ProductEditView(UpdateView):
	template_name = "forms.html"
	model = Product
	fields = ['image', 'name', 'description', 'price', 'available_units', 'category', 'tags']

	def get_success_url(self):
		return reverse('product-edit', kwargs={'pk': self.object.id})

class PendingOrdersView(TemplateView):
	template_name = "dashboard/pendingorders.html"