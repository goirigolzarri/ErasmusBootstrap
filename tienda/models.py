from django.db import models
from django.urls import reverse
from members.models import User

# Create your models here.

class CategoriaProducto(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class ColorProducto(models.Model):
	name = models.CharField(max_length=15)
	
	def __str__(self):
		return self.name

class Tallas(models.Model):

	name = models.CharField(max_length=15)

	def __str__(self):
		return self.name

class Bandera(models.Model):

	foto = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default.png')
	name = models.CharField(max_length=15)

	def __str__(self):
		return self.name







	
class Product(models.Model):
	foto = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default.png')
	foto2 = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default2.png')
	foto3 = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default3.png')
	foto4 = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default4.png')
	name = models.CharField(max_length=30, null=False, blank=False, default='Producto Erasmus Planet')
	codigo = models.CharField(max_length=10, null=False, blank=False)
	precio = models.FloatField(default=10.00)
	detalles = models.CharField(max_length=50, null=True) 
	categoria = models.ForeignKey(CategoriaProducto, on_delete=models.SET_NULL, null = True)
	colores = models.ManyToManyField('ColorProducto', related_name='products')
	tallas = models.ManyToManyField('Tallas', related_name='products')
	bandera = models.ManyToManyField('Bandera', related_name='products')
	
	
	
	def get_absolute_url(self):
		return reverse('Tienda')

	def __str__(self):
		return self.name


	@property
	def fotoURL(self):
		try:
			url = self.foto.url
		except:
			url = ''
		return url

	@property
	def foto2URL(self):
		try:
			url = self.foto2.url
		except:
			url = ''
		return url
	@property
	def foto3URL(self):
		try:
			url = self.foto3.url
		except:
			url = ''
		return url
	@property
	def foto4URL(self):
		try:
			url = self.foto4.url
		except:
			url = ''
		return url





class Customer(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):

		return str(self.id)

class Order(models.Model):
    
	pedido_de = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True, blank=False)
	transaction_id = models.CharField(max_length=200, null=True)


	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total








class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	
	talla = models.CharField(null= True, blank=True,  max_length=20)
	bandera = models.CharField(null=True, max_length=30)
	fecha = models.CharField(null= True, blank=True,  max_length=20)
	color = models.CharField(null= True, blank=True,  max_length=20)

	@property
	def get_total(self):
		total = self.product.precio * self.quantity
		return total


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.address


