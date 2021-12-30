from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete=models.SET_NULL)
    device_id = models.CharField(max_length = 300, null = True, blank = True)
    profile_picture = models.ImageField(null=True)
    first_name = models.CharField(max_length = 250, null = True)
    last_name = models.CharField(max_length = 250, null = True)
    email = models.EmailField(max_length = 250, null = True, blank = True)
    address_line_1 = models.CharField(max_length = 250, null = True)
    address_line_2 = models.CharField(max_length = 250, null = True, blank = True)
    city = models.CharField(max_length = 250, null = True)
    state = models.CharField(max_length = 250, null = True)
    country = models.CharField(max_length = 250, default = "Nigeria")
    postal_code = models.PositiveIntegerField(null = True)
    phone_number = PhoneNumberField()
    slug = AutoSlugField(populate_from='__str__')

    def __str__(self):
    	if self.user:
    		name = self.user.username
    	else:
    		name = self.device_id
    	return str(name)

class DeliveryAddress(models.Model):
    customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    first_name = models.CharField(max_length = 250, null = True)
    last_name = models.CharField(max_length = 250, null = True)
    email = models.EmailField(max_length = 250, null = True, blank = True)
    address_line_1 = models.CharField(max_length = 250, null = True)
    address_line_2 = models.CharField(max_length = 250, null = True, blank = True)
    city = models.CharField(max_length = 250, null = True)
    state = models.CharField(max_length = 250, null = True)
    country = models.CharField(max_length = 250, default = "Nigeria")
    postal_code = models.PositiveIntegerField(null = True)
    phone_number = models.PositiveIntegerField(null = True)

class DefaultAddress(models.Model):
    customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    DeliveryAddress = models.ForeignKey(DeliveryAddress, null = True, on_delete = models.SET_NULL)