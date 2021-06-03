from django import forms
from .models import *


choices_city = City.objects.all().values_list('name', 'name')
city_list = []

for item in choices_city:
	city_list.append(item)

class AñadirGuia(forms.ModelForm):

    class Meta:
        model = Guide
        fields = ('city', 'title', 'informacion_general','como_llegar', 'comida',
         'alojamiento', 'ocio', 'divisas', 'banco_sim', 'donde_comprar')

        widgets ={
			
            'city': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'title': forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'informacion_general': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'como_llegar': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'comida':forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'alojamiento': forms.Textarea(attrs={'class':'form-control ', 'value': '', 'type': 'hidden'}),
			'ocio': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'divisas': forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'banco_sim': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'donde_comprar': forms.Textarea(attrs={'class':'form-control ', 'placeholder': 'First name...'}),
			


        }

class EditarGuia(forms.ModelForm):

    class Meta:
        model = Guide
        fields = ('city', 'title','informacion_general','como_llegar', 'comida',
         'alojamiento', 'ocio', 'divisas', 'banco_sim', 'donde_comprar')

        widgets ={
			
            'city': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'title': forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'informacion_general': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'como_llegar': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'comida':forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'alojamiento': forms.Textarea(attrs={'class':'form-control ', 'value': '', 'type': 'hidden'}),
			'ocio': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'divisas': forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'banco_sim': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'donde_comprar': forms.Textarea(attrs={'class':'form-control ', 'placeholder': 'First name...'}),
			


        }



class ContactForm(forms.Form):
	first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Your firstname...'}))
	last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Your lastname...'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control ', 'placeholder': 'Email...'}))
	subject = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Subject...'}))
	body = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class':'form-control ', 'placeholder': 'Say something about us...'}))

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['first_name']
		self.fields['last_name']
		self.fields['email']
		self.fields['subject']
		self.fields['body']