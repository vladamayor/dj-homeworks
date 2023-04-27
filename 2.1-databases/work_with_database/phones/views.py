from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_obj = Phone.objects.all()
    context = {
        'phones': phone_obj
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_obj = Phone.objects.filter(slug=slug)
    context = {
        'phone': phone_obj
    }
    return render(request, template, context)
