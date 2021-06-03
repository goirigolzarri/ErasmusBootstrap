
from descuentosApp.models import Country, University
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm

from members.models import User
from django import forms
from .models import City, Country




# Cargar SubCategorias
choices_sub = City.objects.all().values_list('name', 'name')
city_list = []

for item in choices_sub:
	city_list.append(item)


choices_country = Country.objects.all().values_list('name', 'name')
country_list = []

for item in choices_country:
	country_list.append(item)

#generos
gender_list=['Male ', 'Female', 'Unisex']

course_list=['1 ', '2', '3', '4 ', '5', '6']

class SignUpForm(UserCreationForm):
	email =forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name','city', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
			  
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'


STUDENT_CHOICES = (('1', 'Bachelor'), ('2', 'Au Pair'), ('3', 'Master'), ('4', 'Internship')),

class CreateUserForm(UserCreationForm):
	
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'date' , 'date_inicio', 'date_fin', 'gender' ,'country', 'phone', 'prefix', 'studentType', 'cityOrigin1',
		 'cityDestination1', 'cityDestination2', 'cityDestination3', 'universityOrigin', 'universityDestination', 'studies', 'email', 'password1', 'password2', 'course', 'company']
		
		def __init__(self, *args, **kwargs):
			super(CreateUserForm, self).__init__(*args, **kwargs)
			# asi vuelves tus campos no requeridos
			self.fields['course'].required = False

		widgets ={
			
            'cityDestination1': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'cityDestination2': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'cityDestination3': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'cityOrigin1': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'universityOrigin': forms.Select(attrs={'class':'form-control '}),
			'studentType': forms.TextInput(attrs={'class':'form-control ', 'value': '', 'type': 'hidden'}),
			'universityDestination': forms.Select(attrs={'class':'form-control '}),
			'country': forms.Select(choices=country_list, attrs={'class':'form-control '}),
			'gender': forms.Select(choices=gender_list, attrs={'class':'form-control '}),
			'first_name': forms.TextInput(attrs={'class':'form-control '}),
			'last_name': forms.TextInput(attrs={'class':'form-control '}),
			'date': forms.DateInput(attrs={'class':'form-control ', 'type' :'date'}),
			'username': forms.TextInput(attrs={'class':'form-control '}),
			'email': forms.EmailInput(attrs={'class':'form-control ', 'placeholder': 'name@example.com'}),
			'prefix': forms.TextInput(attrs={'class':'form-control ', 'placeholder': '+34'}),
			'phone': forms.TextInput(attrs={'class':'form-control '}),
			'studies': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Example: Business Administration'}),
			'course': forms.Select(choices=course_list, attrs={'class':'form-control '}),
			'company': forms.TextInput(attrs={'class':'form-control '}),
			'date_inicio': forms.TextInput(attrs={'class':'form-control ', 'placeholder': '05/2021'}),
			'date_fin': forms.TextInput(attrs={'class':'form-control ', 'placeholder': '12/2021'}),
			

		
		}

university_choices = University.objects.all().values_list('name', 'name')
university_list = []

for uni in university_choices:
	university_list.append(uni)

class EditUserForm(UserChangeForm):
	
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'date' , 'gender' ,'country', 'phone', 'studentType', 'cityOrigin1',
		 'cityDestination1', 'cityDestination2', 'cityDestination3', 'universityOrigin', 'universityDestination', 'studies', 'email', 'course', 'company']
		
			  

		widgets ={
			
            'cityDestination1': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'cityDestination2': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'cityDestination3': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'cityOrigin1': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'universityOrigin': forms.Select(choices=university_list,attrs={'class':'form-control '}),
			'studentType': forms.TextInput(attrs={'class':'form-control ', 'value': '', 'type': 'hidden'}),
			'universityDestination': forms.Select(choices=university_list,attrs={'class':'form-control '}),
			'country': forms.Select(choices=country_list, attrs={'class':'form-control ', 'default':False}),
			'gender': forms.Select(choices=gender_list, attrs={'class':'form-control '}),
			'first_name': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'First name...'}),
			'last_name': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Last name...'}),
			'date': forms.DateInput(attrs={'class':'form-control ', 'type' :'date', 'placeholder': 'Birthday...'}),
			'username': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Username...'}),
			'email': forms.EmailInput(attrs={'class':'form-control ', 'placeholder': 'Email...'}),
			'phone': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Phone number...'}),
			'studies': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Studies...'}),
			'course': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Course...'}),
			'company': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Company...'}),
			

		
		}



# Form para cambiar la contra
class ChangePassword(PasswordChangeForm):

	pedido_de =  forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': '*****'})),
	pedido =  forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': '*****'})),
	direccion =  forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': '*****'})),
	new_password2 =  forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': '*****'})),
	new_password1 =  forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': '*****'})),
	new_password1 =  forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': '*****'})),
	new_password1 =  forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': '*****'})),
	new_password1 =  forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': '*****'})),

	class Meta:
		model = User
		fields = ['pedido_de', 'pedido', 'direccion', 'ciudad', 'provincia', 'codigo_postal', 'date_added' ]