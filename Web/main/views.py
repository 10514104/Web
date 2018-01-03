from django.shortcuts import render, get_object_or_404

from product.models import Product


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'main/main.html',context)



def mainProduct(request, productId):
    '''
    Read an article
        1. Get the "article" instance using "articleId"; redirect to the 404 page if not found
        2. Render the articleRead template with the article instance and its
           associated comments
    '''
    product = get_object_or_404(Product, id=productId)
    products = Product.objects.all()
    context = {'product': product,'products':products}
    return render(request, 'main/mainProduct.html', context)


