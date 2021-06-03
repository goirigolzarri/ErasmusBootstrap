from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import request
from django.urls.base import reverse
from django.urls.conf import path
from descuentosApp.models import Country
from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth.forms import *
from django.urls import reverse_lazy
from .forms import *
from .models import User
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import EmailMessage


# Imports para el email verification

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator






def NewUserRegistrationView(request):
    error = False
    form = CreateUserForm()
    if request.method == 'POST':

        form = CreateUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_active = False
            edadintro = instance.date
            edad = instance.calcularEdad(edadintro)

            if (edad > 18):
                
                instance.save()

                

                # Email
                email_subject = 'Activate your account'
                # Path a la ventana

                uidb64 = urlsafe_base64_encode(force_bytes(instance.pk))

                domain = get_current_site(request).domain
                link = reverse('ActivateAcount', kwargs = {'uidb64': uidb64, 'token': token_generator.make_token(instance)})
                activate_url = 'http://'+domain+link
                email_body = 'Hola' + instance.username + 'please, use this link to validate your email\n' + activate_url
                email = EmailMessage(
                    email_subject, 
                    email_body,
                    'noreply@semycolon.com', 
                    [instance.email],
                    
                )
                email.send(fail_silently=True)

                return redirect ('base')
            else: 
                error = True

    context = {'form': form, 'error': error}
    return render (request, 'registration/registration.html', context)



class Verification(View):
    def get(self, request, uidb64, token):


        try:
            id=force_text(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=id)

            if not token_generator.check_token(user, token):
                return redirect('Login' + '?message=' + 'User al ready activated')


            if user.is_active:
                return redirect('Login')

            user.is_active = True 
            user.save()

            messages.success(request, 'Account activated sucesfully')
            return redirect('Login')

        except Exception as ex:
            pass



        
        return redirect('Login')











def Login(request):

  
    if request.method == 'POST':

        if request.POST.get('submit') == 'sign_in':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('base')



    return render(request, 'registration/login.html')


 





@login_required
def UserProfile(request):

    return render(request, 'profile/userProfile.html')


class EditProfile(UpdateView):

    form_class = EditUserForm
    template_name = 'profile/edit_profile.html'
    success_url = reverse_lazy('base') #METER PLANTILLA DE SUCCESFULL EDIT.
    
    

    def get_object(self):
        return self.request.user



class PasswordChangeView(PasswordChangeView):

    form_class = ChangePassword
    template_name = 'perfil/change_password.html'
    succes_url = reverse_lazy('Index')
    
