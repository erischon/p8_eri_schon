from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError

def signupuser(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('moncompte')
            except IntegrityError:
                return render(request, 'users/signup.html', {'form':UserCreationForm(), 'error':'Cet email est déjà pris. Merci d\'en choisir un nouveau.'})
        else:
            return render(request, 'users/signup.html', {'form':UserCreationForm(), 'error':'Les mots de passe ne sont pas identiques.'})
    else:
        return render(request, 'users/signup.html', {'form':UserCreationForm()})

def loginuser(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('moncompte')
            except IntegrityError:
                return render(request, 'users/signup.html', {'form':UserCreationForm(), 'error':'Cet email est déjà pris. Merci d\'en choisir un nouveau.'})
        else:
            return render(request, 'users/signup.html', {'form':UserCreationForm(), 'error':'Les mots de passe ne sont pas identiques.'})
    else:
        return render(request, 'users/login.html', {'form':AuthenticationForm()})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def moncompte(request):
    return render(request, 'users/moncompte.html')