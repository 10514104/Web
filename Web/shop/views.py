from django.shortcuts import render, redirect

from product.models import Product

# Create your views here.

def shop(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'shop/shop.html',context)