from django.contrib import admin
from .models import *
from members.models import *

from adminErasmus.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Modelos de Tienda
from tienda.models import *
# Register your models here.


class CountryAdmin(ImportExportModelAdmin):
	pass

class GuideAdmin(ImportExportModelAdmin):
	pass
class CityAdmin(ImportExportModelAdmin):
	pass

class OrderInstanceInline(admin.TabularInline):
	model = Order
	ordering = ('complete', )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('first_name','username','email',)
	search_fields = ('username', 'first_name')
	list_filter = ('studentType',)
	fieldsets = (
		('Credenciales', {
			'fields': ('username','email', 'password', 'last_login', )
		}),
		('Permisos', {
			'fields': ('is_staff', 'is_superuser',)
		}),
		('Datos personales', {
			'fields': ('first_name', 'gender', 'phone', 'country',)
		}),
		('Datos de estudios', {
			'fields': ('studentType','cityOrigin1', 'cityDestination1', 'cityDestination2', 'cityDestination3', 'universityOrigin', 'universityDestination', 'studies', 'company')
		}),
	)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('id','name','email','user',)
	search_fields = ('name', 'user')
	fieldsets = (
		('Datos', {
			'fields': ('name', 'user', )
		}),
	  
	)
   
	inlines = [OrderInstanceInline]
	


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('codigo','name','precio', 'detalles','categoria','descuento','stock',)
	search_fields = ('name', 'user')
	fieldsets = (
		('Referencia', {
			'fields': ('codigo','name')
			
		}),('Datos', {
			'fields': ('precio','stock','descuento', )
			
		}),('Caracteristicas', {
			'fields': ('detalles','categoria', 'colores','tallas',)
			
		}),
	  
	) 



admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(University)
admin.site.register(Guide, GuideAdmin)











admin.site.register(ColorProducto)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(CategoriaProducto)
admin.site.register(Tallas)
admin.site.register(Bandera)
admin.site.register(Descuento)


