from django.shortcuts import render, redirect

from product.models import Product
from product.models import Shop

# Create your views here.

def shop(request):
    products = Product.objects.all()
    shops = Shop.objects.all()
    context = {'products':products,'shops':shops,}
    return render(request, 'shop/shop.html',context)

def checkout(request):
    Delivery = request.POST.get('Delivery')
    payment = request.POST.get('payment')
    products = Product.objects.all()
    shops = Shop.objects.all()
    context = {'products':products,'shops':shops,'payment':payment,'Delivery':Delivery}
    return render(request, 'shop/checkout.html',context)