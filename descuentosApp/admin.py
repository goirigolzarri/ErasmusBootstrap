from django.contrib import admin
from .models import *
from members.models import *

from adminErasmus.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class CountryAdmin(ImportExportModelAdmin):
	pass

class GuideAdmin(ImportExportModelAdmin):
	pass
class CityAdmin(ImportExportModelAdmin):
	pass

admin.site.register(User)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(University)
admin.site.register(Guide, GuideAdmin)






# Modelos de Tienda
from tienda.models import *


admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(ColorProducto)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(CategoriaProducto)
admin.site.register(Tallas)
admin.site.register(Bandera)


