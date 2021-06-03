from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [


    path('tienda/', views.Tienda, name='Tienda'),
	path('carrito/', views.Carrito, name='Carrito'),
    path('checkout/', views.Checkout, name='Checkout'),
    path('producto/<int:pk>', views.ProductDetail.as_view(), name='ProductDetail'),
    path('update_item/', views.updateItem, name='update_item'),
    
    path('process_order/', views.processOrder, name='processOrder'),

    
]