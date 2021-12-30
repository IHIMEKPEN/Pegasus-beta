from product.models import *
from django.views.generic import ListView
def say_hello(request):
	return {"hello": "Hello there"}

def new_orders(request):
	orders = Order.objects.filter(completed = True)
	pending_orders = []
	shipping_orders = []
	delivered_orders = []
	for order in orders:
		if order.status == "DELIVERED":
			delivered_orders.append(order)
		elif order.status == "SHIPMENT":
			shipping_orders.append(order)
		else:
			pending_orders.append(order)
	length = str(len(pending_orders))
	context = {"pending_order_count": length, "pending_orders": pending_orders,}
	return context
