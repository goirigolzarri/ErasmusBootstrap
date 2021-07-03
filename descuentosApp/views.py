from typing import ContextManager, final
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
from django.core.paginator import Page, Paginator
from .utils import merge_two_dicts
import time
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


	# data = request.POST.getlist('city')
	# print(data)
	alojamientos_cached = ('alojamientos' in request.session)
	if alojamientos_cached: print('Ciudades en cache!')
	if not alojamientos_cached:

		response = requests.get('http://cdn.housinganywhere.com/feeds/happyerasmusbilbao/happyerasmusbilbao.json')
	
		api = response.json()
		data = api['listings']
		request.session['alojamientos'] = data


	
	alojamientos = request.session['alojamientos']


	ciudades_cached = ('ciudades'  in request.session)
	if ciudades_cached:
		print('tiene ciudades!')
		
	else:
		try:
			ciudades = []
			# data = api['listings']
			for alojamiento in alojamientos:

				ciudades.append(alojamiento['location']['city'])
				print('Ciudades:', alojamiento['location']['city'])
				

			ciudades = list(set(ciudades)) 
			ciudades = sorted(ciudades)
			print(len(ciudades))
			print('Lista de ciudades:',ciudades)
			request.session['ciudades'] = ciudades
		


		except Exception as e:
			print(e)




	ciudades = request.session['ciudades']
	ciudades = list(set(ciudades)) 
	ciudades = sorted(ciudades)



	city = request.POST.getlist('city')
	print(str(city))

	string = ' '.join([str(item) for item in city])
	print(string)

	if city:
		alojamientos_busqueda = [] 
		for alojamiento in alojamientos:
			if alojamiento['location']['city'] == string:
				alojamientos_busqueda.append(alojamiento)
			

	if alojamientos_busqueda == None:
		paginator = Paginator(alojamientos, 25)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context = {'page_obj': page_obj, 'ciudades': ciudades}
	else:

		paginator = Paginator(alojamientos_busqueda, 25)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context = {'page_obj': page_obj, 'ciudades': ciudades}


	return render(request , 'api.html', context)



def Uniplaces(request):
	city = request.POST.getlist('city')
	print(str(city))

	string = ' '.join([str(item) for item in city])
	print(string)
	headers_dict = {'x-api-key':'XSbb5cQ5KmaUXiJc6975BadCW3WGu1nwaQIL8tLA'}



	response_citys = requests.get('https://api.staging-uniplaces.com/v1/cities', headers=headers_dict)
	api_citys = response_citys.json()
	context = {'api_citys':api_citys}

	if city:
		response = requests.get('https://api.staging-uniplaces.com/v1/cities/' + string + '/offers', headers=headers_dict)
		api = response.json()
		data = api['data']
		count = len(data)
		print(count)
		context = {'data':data, 'api_citys':api_citys}


	

	return render(request , context)


def apiTickets(request):

	
	headers = {'Content-Type':'application/json', 'Authorization':'Token KqfEOcJJWSsYmbafLkrLEBR9D7ErzGBO'}
	params = {'lang': 'es'}
	response = requests.get('https://api.tiqets.com/v2/products',params=params ,headers=headers)
	api = response.json()
	
	tiqets = api['products']



	#Descargar cities 
	cities_cached = ('cities' in request.session)
	if cities_cached: print('Ciudades en cache!')
	if not cities_cached:
		cities_dict = []
		page = 1
		headers = {'Content-Type':'application/json', 'Authorization':'Token KqfEOcJJWSsYmbafLkrLEBR9D7ErzGBO'}
		params = {'lang': 'en', 'page': page}
		response = requests.get('https://api.tiqets.com/v2/cities',params=params ,headers=headers)
		pages_data = response.json()
		pages = pages_data['pagination']['total']
		print(pages)
		time.sleep(1)
		for page_num in range(1,141):
			print('Pagina:', page_num)

			params = {'lang': 'es', 'page': page_num}
			response = requests.get('https://api.tiqets.com/v2/cities',params=params ,headers=headers)
			respuesta = response.json()
			cities = respuesta['cities']
			
			

			for city in cities:
				cities_dict.append(city)

	
		request.session['cities'] = cities_dict

	

	cities = request.session['cities']
	cities = sorted(cities, key=lambda k: k['name'])
	context = {'tiqets': tiqets, 'cities': cities}

	city = request.POST.getlist('city')
	print(str(city))

	string = ' '.join([str(item) for item in city])
	print(string)

	if city:
		tiqets = []
		headers = {'Content-Type':'application/json', 'Authorization':'Token KqfEOcJJWSsYmbafLkrLEBR9D7ErzGBO'}
		params = {'lang': 'es','city_id': string }
		response = requests.get('https://api.tiqets.com/v2/products',params=params ,headers=headers)
		search_data = response.json()
		data = search_data['products']
		total = search_data['pagination']['total']
		for dat in data:

			tiqets.append(dat)
		
		for page_num in range(1, total//10):
			headers = {'Content-Type':'application/json', 'Authorization':'Token KqfEOcJJWSsYmbafLkrLEBR9D7ErzGBO'}
			params = {'lang': 'es','city_id': string }
			response = requests.get('https://api.tiqets.com/v2/products',params=params ,headers=headers)
			response_data = response.json()
			data = response_data['products']
			for dat in data:

				tiqets.append(dat)
			





		context = {'tiqets': tiqets, 'cities': cities}


	return render(request , 'apiTickets.html', context)


	
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