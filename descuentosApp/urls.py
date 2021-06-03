from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import autosuggest


urlpatterns = [

	path('',views.base, name='base'),
	path('index/',views.index, name='index'),
	path('city-list/', views.CityList, name='CityList'),
	path('descuentos/', views.Descuentos, name='Descuentos'),
	path('alojamiento/', views.Alojamiento, name='Alojamiento'), 
    path('adminsite/', views.AdminSite, name='Admin'), 
    path('adminsite/addguide', views.AddGuide.as_view(), name='AddGuide'), 
	path('guia/<int:pk>', views.Guia.as_view(), name='Guia'),
	path('adminsite/editguide/<int:pk>', views.EditGuide.as_view(), name='EditGuide'),
    path('adminsite/deleteguide/<int:pk>', login_required(views.DeleteGuide.as_view()), name='DeleteGuide'),
    
 
	path('contacto/', views.Contacto, name='Contacto'),
	path('propuesta_guia/', views.Propuestaguia, name='Propuestaguia'),
	path('privacyPolicy/', views.PrivacyPolicy, name='PrivacyPolicy'),
	path('faq/', views.Faq, name='Faq'),
	path('api/', views.api, name='api'),
    path('autosuggest/', autosuggest, name='autosuggest')


]