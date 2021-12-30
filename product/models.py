from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from account.models import *

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=150)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name
		
		

class Product(models.Model):
	name = models.CharField(max_length=150)
	image = models.ImageField(null = True)
	description = models.TextField(null=True, blank=True)
	price = models.PositiveIntegerField()
	category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
	tags = models.ManyToManyField(Tag, blank=True)
	available_units = models.PositiveIntegerField(blank=False, default=1)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

# The order model
class Order(models.Model):
	SORTING = 'SORTING'
	SHIPMENT = 'SHIPMENT'
	DELIVERED = 'DELIVERED'
	STATUS_CHOICES = [
		(SORTING, 'Sorting'),
		(SHIPMENT, 'In Transit'),
		(DELIVERED, 'Delivered'),
	]
	customer = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)
	completed = models.BooleanField(default = False, null = True, blank = True)
	transaction_id = models.CharField(max_length = 200, null = True, blank = True)
	status = models.CharField(max_length = 20, choices = STATUS_CHOICES, null = True, blank = True)

	@property
	def reference(self):
		return self.customer.__str__() + str(self.id)
	
	@property
	def total(self):
		total = 0
		for cartitem in self.cartitem_set.all():
			total += cartitem.get_price()
		return total

	def __str__(self):
		return self.customer.__str__()
		
#cart item model
class CartItem(models.Model):
	product = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
	units = models.PositiveIntegerField(default = 0, blank = True,)
	customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	order = models.ForeignKey(Order, null = True, on_delete = models.SET_NULL)
	date_added = models.DateTimeField(auto_now_add=True)

	def max_unit(self):
		return self.product.available_units
	
	def get_price(self):
		return int((self.product.price * self.units))

	def __str__(self):
		return self.product.name

