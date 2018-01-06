from django.shortcuts import render, redirect

from product.models import Product
from product.models import Shop

# Create your views here.

def shop(request):
    products = Product.objects.all()
    shops = Shop.objects.all()
    context = {'products':products,'shops':shops}
    return render(request, 'shop/shop.html',context)



def checkout(request):
    Delivery = request.GET.get('Delivery')
    payment = request.GET.get('payment')
    products = Product.objects.all()
    shops = Shop.objects.all()
    context = {'products':products,'shops':shops,
               'payment':payment,'Delivery':Delivery,}
    return render(request, 'shop/checkout.html',context)



def order(request):
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    address = request.GET.get('address')
    remark = request.GET.get('remark')
    Delivery = request.GET.get('Delivery')
    payment = request.GET.get('payment')
    products = Product.objects.all()
    shops = Shop.objects.all()
    print(Delivery,payment)
    context = {'products':products,'shops':shops,'name':name
               ,'phone':phone,'address':address,'remark':remark
               ,'Delivery':Delivery,'payment':payment}
    return render(request, 'shop/order.html',context)


