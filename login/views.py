# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


def login(request):
    if not request.POST:
        return render(request, 'login.html')
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
 

def register(request):
    user_create_form = UserCreationForm()
    if not request.POST:
        return render(request, 'register.html', {'form': user_create_form})
    new_user_form = UserCreationForm(request.POST)
    if new_user_form.is_valid():
        new_user_form.save()
        new_user = auth.authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password1'])
        auth.login(request, new_user)
        return redirect('/')
    else:
        user_create_form = new_user_form
    return render(request, 'register.html', {'form': user_create_form})


