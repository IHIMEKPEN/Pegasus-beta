from django.shortcuts import render, reverse
from product.models import *
from account.models import Customer
from django.http import HttpResponse, JsonResponse
from django.views.generic import UpdateView
import requests
import json
import datetime
import os



# PAYSTACK_API_KEY = os.environ.get('PAYSTACK_API_KEY')
PAYSTACK_API_KEY='sk_test_0158289ec20709947f87b5fcd317daa1579d46de'

HEADERS = {
    "Authorization": "Bearer "+ PAYSTACK_API_KEY,
}

# Create your views here.
class DeliveryInfo(UpdateView):
	template_name = "forms.html"
	
	def get_object(self):
		user = self.request.user
		deviceId = self.request.COOKIES["deviceId"]
		try:
			customer = Customer.objects.get(user = user)
		except:
			customer, created = Customer.objects.get_or_create(device_id = deviceId)
		return customer
	fields = ['first_name', 'last_name', 'email', 'address_line_1', 'address_line_2', 'city', 'state', 'country', 'postal_code', 'phone_number']
	def get_success_url(self):
		return reverse('checkout') 


def CheckoutView(request):
	template = "checkout.html"
	try:
		customer= Customer.objects.get(user = request.user)
	except:
		deviceId = request.COOKIES["deviceId"]
		customer, created = Customer.objects.get_or_create(device_id = deviceId)
	order, created = Order.objects.get_or_create(customer = customer, completed = False)
	string = str(datetime.datetime.now().timestamp())
	order.transaction_id = string
	order.save()
	
	print(order.transaction_id)
	cartitems = order.cartitem_set.all()
	return render(request, template, {"order":order,
	"cartitems":cartitems})

def InitializePaymentView(request):
	data = json.loads(request.body)
	res = requests.post('https://api.paystack.co/transaction/initialize', json = data, headers = HEADERS)
	print (res.text)
	response = res.json()
	print (response)
	return JsonResponse(response)

def VerifyPaymentView(request, *args, **kwargs):
	reference = request.GET['trxref']
	order = Order.objects.get(transaction_id = reference)
	#print (reference)
	url = 'https://api.paystack.co/transaction/verify/'
	verify_url = url + reference
	res = requests.get(verify_url, headers=HEADERS)
	response = res.json()
	if res.ok == True:
	    content = json.loads(res.content)
	    message = content["message"]
	    if message == "Verification successful":
	        order.completed = True
	        order.save()
	else:
	    message = "Operation failed"
	#print (message)
	return HttpResponse(message)