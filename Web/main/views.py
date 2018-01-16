from django.shortcuts import render, get_object_or_404, redirect

from product.models import Product,Shop


def main(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'main/main.html',context)



def mainProduct(request, productId):
    product = get_object_or_404(Product, id=productId)
    products = Product.objects.all()
    context = {'products':products,'product':product}
    if request.method == 'GET':
        return render(request, 'main/mainProduct.html',context)
    #POST
    amount = int(request.POST.get('amount'))
    shop = Shop()
    shop.name = product.name
    shop.price = product.price
    shop.amount = amount
    shop.save()
    return redirect('main:main')


