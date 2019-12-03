# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        'title': 'Register'
    }

    return render(request, 'users/register.html', context)

