from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [


	path('register/', views.NewUserRegistrationView, name='UserRegistrationView'),
	

	path('login/', views.Login, name='Login'),
	path('userprofile/', views.UserProfile, name='UserProfile'), 
	path('edituserprofile/', login_required(EditProfile.as_view()), name='EditUserProfile'), 
	path('password/', login_required(PasswordChangeView.as_view(template_name = 'profile/change_password.html')), name='ChangePassword'),
   # path('register/', views.Register, name='Register'),

	# Validate Email
	path('activate/<uidb64>/<token>', Verification.as_view(), name='ActivateAcount' ),


	#Reseteo de la contra via email: 
	path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'profile/email_password_reset.html'), name="reset_password"),
	path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'profile/password_reset_sent.html' ), name="password_reset_done"), 
	path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'profile/password_reset_form.html'), name="password_reset_confirm"),
	path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'profile/password_reset_done.html'), name="password_reset_complete"), 
]