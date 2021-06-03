from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields import CharField
from django.urls import reverse


# Create your models here.


class Country(models.Model):

	name = models.CharField(max_length=30)

	class Meta:
        
		ordering = ['name']



	def __str__(self):

		return self.name





class City(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)


	def __str__(self):

		return self.name

	def get_absolute_url(self):
		return reverse('City')



class University(models.Model):
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)



	def __str__(self):

		return self.name



class Guide(models.Model):
	
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, default='')
	informacion_general = RichTextField(blank=True)
	como_llegar = RichTextField(blank=True)
	comida = RichTextField(blank=True, default = '')
	alojamiento = RichTextField(blank=True)
	ocio = RichTextField(blank=True)
	divisas = RichTextField(blank=True)
	banco_sim = RichTextField(blank=True)
	donde_comprar = RichTextField(blank=True)
	foto = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default.png')
	foto2 = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default.png')
	foto3 = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default.png')
	foto4 = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default.png')
	foto5 = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default.png')
	foto6 = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default.png')
	foto7 = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default.png')
	

	def __str__(self):

		return self.title



