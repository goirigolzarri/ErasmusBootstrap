from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import DeleteView
from .models import Guide, City
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.db.models import Q
from .forms import AñadirGuia, ContactForm, EditarGuia
from django.template.loader import get_template
from django.core.mail import EmailMessage
from tienda.models import *
from django.http import JsonResponse
import requests
import json
from django.core.paginator import Paginator
# Create your views here.


def base(request):

	# from django.utils import translation
	# user_language = 'es'
	# translation.activate(user_language)
	# request.session[translation.LANGUAGE_SESSION_KEY] = user_language
	# if translation.LANGUAGE_SESSION_KEY in request.session:
	# del request.session[translation.LANGUAGE_SESSION_KEY]

	model = Guide
	city_list = City.objects.all()
	guiasTarjetas = Guide.objects.all()

	queryset = request.GET.get("search")
	guides = Guide.objects.all()
	query = False
	errormessage = 'Todavia no trabajamos ahi'

	if queryset:

		guides = Guide.objects.filter(Q(title__icontains=queryset)).distinct()
		if not guides:
			query = True
		else:
			context = {'guides': guides}
			query = True

	return render(request, 'base.html', {'guides': guides, 'query': query, 'guiasTarjetas': guiasTarjetas})


def CityList(request):

	city_list = City.objects.all()
	return render(request, 'city_list.html', {'city_list': city_list})


def Descuentos(request):

	return render(request, 'descuentos.html')


def Alojamiento(request):

	return render(request, 'alojamiento.html')


def AdminSite(request):

	guides = Guide.objects.all()
	context = {'guides': guides}

	return render(request, 'admin.html', context)


class AddGuide(CreateView):
	model = Guide
	form_class = AñadirGuia
	template_name = 'add_guide.html'

	success_url = reverse_lazy('Admin')


class EditGuide(UpdateView):
	model = Guide
	form_class = EditarGuia
	template_name = 'edit_guide.html'

	success_url = reverse_lazy('Admin')


class DeleteGuide(DeleteView):

	model = Guide
	template_name = 'delete_guide.html'
	success_url = reverse_lazy('Admin')


class Guia(DetailView):

	model = Guide
	template_name = 'guia.html'


def Contacto(request):

	form = ContactForm()
	context = {'form': form}

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():

			firstname = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			subject = request.POST.get('subject')
			body = request.POST.get('body')

			context = {
				'firstname': firstname,
				'last_name': last_name,
				'email': email,
				'subject': subject,
				'body': body,
			}
			template = get_template('contacto.txt')
			
			content = template.render(context)

			email = EmailMessage(
				"Contact Page / " + subject,
				content,
				"Erasmus Planet" +'',
				['erasmuusplanet@gmail.com'],
				headers = {'Reply-To': email }
			)
			email.send()
			
			return redirect('base')




	return render(request, 'contacto.html', context)

def Propuestaguia(request):

	return render(request, 'propuestaguia.html')

def PrivacyPolicy(request):

	return render(request, 'privacyPolicy.html')

def Faq(request):

	return render(request, 'faq.html')


def index(request):

	if request.user.is_authenticated:
		logged_in_user = request.user
		order, created = Order.objects.get_or_create(pedido_de=logged_in_user, complete = False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0}
		cartItems = order['get_cart_items']

	

	context = {'items': items, 'order': order, 'cartItems': cartItems}

	return context


def api(request):

	response = requests.get('http://cdn.housinganywhere.com/feeds/happyerasmusbilbao/happyerasmusbilbao.json')
	api = response.json()
	count = api['count']
	print(count)
	data = api['listings']
	#total = len(data)
	#print(total)
	#context = {'data':data, 'count':count}


	paginator = Paginator(data, 25)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	


	return render(request , 'api.html', {'page_obj': page_obj})

	
def autosuggest(request):
	print(request.GET)
	query_original = request.GET.get('term')
	queryset = Guide.objects.filter(title__icontains=query_original)
	print(queryset)
	mylist= []
	mylist += [x.title for x in queryset]
	print(mylist)
	return JsonResponse(mylist,safe=False)

# def api(request):
# 	file = open(r'C:\Users\Asier\Documents\GitHub\ErasmusLocal\swagger.json')
# 	data = file.read()
# 	file.close()
# 	return JsonResponse(data, safe=False)