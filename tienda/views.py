
from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.http import JsonResponse
import json
import datetime
from .utils import cartData, cookieCart, guestOrder
from django.contrib import messages

# Create your views here.
def Carrito(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items': items, 'order': order, 'cartItems': cartItems}
	return render(request, 'clientes/carrito.html', context)


def Tienda(request):

	productos = Product.objects.all()
	for producto in productos:
		print('Stock virtual ' + producto.name + ':', producto.stock_virtual)

	categorias = CategoriaProducto.objects.all()

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'productos': productos, 'categorias': categorias,'items': items, 'order': order, 'cartItems': cartItems}

	return render(request, 'clientes/tienda.html', context)

def Checkout(request):
	
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']



	context =  {'items': items, 'order': order, 'cartItems': cartItems}
	return render(request, 'clientes/pago.html', context)


class ProductDetail(DetailView):
	model = Product
	template_name = 'clientes/producto.html'


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	color = data['color']
	talla = data['talla']
	
	print('Action:', action)
	print('Product:', productId)

	logged_in_user = request.user
	product = Product.objects.get(id=productId)
	
	print(product.name)
	customer, created = Customer.objects.get_or_create(user=logged_in_user)
	order, created = Order.objects.get_or_create(pedido_de=customer, complete = False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product, color=color, talla=talla)



	if action == 'add':
		if orderItem.product.stock > orderItem.product.stock_virtual:
			orderItem.quantity = (orderItem.quantity + 1)
		else:
			messages.warning(request, 'No stock remaining for ' + orderItem.product.name)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity -1)
			
	orderItem.save()

	if action == 'delete':
		print('Borrar producto')
		orderItem.delete()
	


	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def processOrder(request):

	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		print('error aqui')
		logged_in_user = request.user
		print(logged_in_user)
		customer, created = Customer.objects.get_or_create(user=logged_in_user)
		print(customer)
		order, created = Order.objects.get_or_create(
			pedido_de=customer, complete=False)
		

		


	else:
		customer, order = guestOrder(request, data)
		

	total = float(data['form']['total'])
	order.transaction_id = transaction_id
	if total == float(order.get_cart_total):
		print('LLega hasta el order')
		order.complete = True
		for item in order.items:

			item.product.stock -= item.quantity
			item.product.save()

	order.save()


	ShippingAddress.objects.create(

		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['postalcode'],
	)



	print('Data:', request.body)
	return JsonResponse('Payment submitted..', safe=False)



def ProductCategoria(request, pk):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	categoria = CategoriaProducto.objects.get(id = pk)
	productos = Product.objects.filter(categoria=categoria)
	context = {'categoria': categoria, 'productos':productos,'items': items, 'order': order, 'cartItems': cartItems}

	return render(request, 'clientes/tienda_categoria.html', context)


