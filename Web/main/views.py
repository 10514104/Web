from django.shortcuts import render, get_object_or_404, redirect

from product.models import Product,Shop
from django.contrib import messages


def main(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'main/main.html',context)



def mainProduct(request, productId):
    product = get_object_or_404(Product, id=productId)
    products = Product.objects.all()
    context = {'products':products,'product':product}
    return render(request, 'main/mainProduct.html',context)
    



def mainProduct2(request, productId):
    product = get_object_or_404(Product, id=productId)
    products = Product.objects.all()
    context = {'products':products,'product':product}
    amount = int(request.GET.get('amount'))
    shop = Shop()
    shop.name = product.name
    shop.price = product.price
    shop.amount = amount
    shop.save()
    messages.success(request, '產品已加入購物車。')
    return render(request, 'main/mainProduct.html',context)
    
