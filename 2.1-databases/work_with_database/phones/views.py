from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_obj = Phone.objects.all()
    sort_value = request.GET.get('sort')
    if sort_value == 'min_price':
        phone_obj = phone_obj.order_by('price')
    elif sort_value == 'max_price':
        phone_obj = phone_obj.order_by('-price')
    elif sort_value == 'name':
        phone_obj = phone_obj.order_by('name')
    context = {
        'phones': phone_obj,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    print(phone)
    context = {
        'phone': phone,
    }
    return render(request, template, context)
