from django.shortcuts import render
from django.views.generic import CreateView


def home(request):
    return render(request, 'detail.html')


def contact_us(request):
    return render(request, 'inbox.html')


def about_us(request):
    return render(request, 'new.html')
