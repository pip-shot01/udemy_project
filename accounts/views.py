from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import * 
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

#verification Email
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import EmailMessage 
# from . models import
# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #user activation
            # current_site = get_current_site(request)        #import on top
            # mail_subject = 'please activate your account'
            # message = render_to_string('verification.html', {       
            #     'user': user,
            #     'domain': current_site,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': default_token_generator.make_token(user),
            # })
            # to_email = ('email')
            # send_email = EmailMessage(mail_subject, message, to=[to_email])
            # send_email.send()
            
            messages.success(request, 'Registration successfully done!!!')
            return redirect('index')
        else:
            messages.error(request, form.errors)
            return redirect('register')        
    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'login successfull!!')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid credentials!!')
            return redirect('login')
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request, "you've been logged out!!")
    return redirect('register')

def activate(request):
    return

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='login')
def Forgot_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'password changed successfully')
            return redirect('dashboard')
        else:
            messages.error(request, form.errors)
            return redirect('Forgot_password')
        
    context = {
            'form':form,
            # 'profile':profile,
        }
            
    return render(request, 'Forgot_password.html', context)