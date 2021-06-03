from datetime import date 
from django.db import models
from django.db.models.fields import NullBooleanField
from django.urls.base import reverse

from descuentosApp.models import Country, City, University, Guide
from django.core.validators import RegexValidator

from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    
    date = models.DateField(default="2020-01-01")

    date_inicio = models.CharField(max_length=8, default="")
    
    date_fin = models.CharField(max_length=8, default="")
    
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex'))
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=False)

    COURSE_CHOICES = (('Primero', '1'), ('Segundo', '2'), ('Tercero', '3'), ('Cuarto', '4'), ('Quinto', '5'), ('Sexto', '6'))
    course = models.CharField(max_length=7, choices=COURSE_CHOICES, blank=True, null=True)

    country =  models.ForeignKey(Country, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, )
    prefix = models.IntegerField(null=True )
    STUDENT_CHOICES = (('1', 'Bachelor'), ('2', 'Au Pair'), ('3', 'Master'), ('4', 'Internship'))
    studentType = models.CharField(max_length=10, choices=STUDENT_CHOICES, null=True, default='')
    cityOrigin1 =  models.CharField(max_length=10, blank=True, null=True)
    cityDestination1 =  models.CharField(max_length=50, null=False)
    cityDestination2 =  models.CharField(max_length=50, blank=True)
    cityDestination3 =  models.CharField(max_length=50, blank=True)
    universityOrigin =  models.CharField(max_length=50,null= True, blank=True)
    universityDestination =  models.CharField(max_length=50, null=True, blank=True)
    studies =  models.CharField(max_length=50, null=True, blank=True)
    #course =  models.CharField(max_length=50, null= True, blank=True)
    company = models.CharField(max_length=50,null= True, blank=True)

    def calcularEdad(self, edadintroducida):
        hoy = date.today()
        edad = hoy.year - edadintroducida.year - ((hoy.month, hoy.day) < (edadintroducida.month, edadintroducida.day))

        return edad
    def get_absolute_url(self):
    #return reverse('article-detail', args=(str(self.id)))
     return reverse('base')

    def __str__(self):
        return self.username
   