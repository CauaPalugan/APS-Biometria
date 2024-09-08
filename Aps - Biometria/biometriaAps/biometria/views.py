from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

## Login ##

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate (
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuário não identificado'
            })
        else:
            login(request, user)
            return redirect('vendas')
        
## Cadastro ##

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()

                login(request, user)
                return redirect('vendas')
            
            except:
                return render(request, 'login.html',{
                    'form': UserCreationForm,
                    'error': 'Usuario ja existe!'
                })
        return render(request, 'cadastro.html', {
            'form': UserCreationForm, 
            'error': 'Senhas não batem!'
        })
