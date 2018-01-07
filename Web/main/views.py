from django.shortcuts import render, get_object_or_404, redirect

from product.models import Product
from product.forms import ShopForm


def main(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'main/main.html',context)



def mainProduct(request, productId):
    product = get_object_or_404(Product, id=productId)
    products = Product.objects.all()
    context = {'products':products,'product':product,'shopForm':ShopForm()}
    if request.method == 'GET':
        return render(request, 'main/mainProduct.html',context)
    #POST
    shopForm = ShopForm(request.POST)
    shopForm.save()
    return redirect('main:main')


