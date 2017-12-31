from django.shortcuts import render, get_object_or_404

from product.models import product


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    products = product.objects.all()
    context = {'products':products}
    return render(request, 'main/main.html',context)



def mainProduct(request, productId):
    '''
    Read an article
        1. Get the "article" instance using "articleId"; redirect to the 404 page if not found
        2. Render the articleRead template with the article instance and its
           associated comments
    '''
    Product = get_object_or_404(product, id=productId)
    products = product.objects.all()
    context = {'product': Product,'products':products}
    return render(request, 'main/mainProduct.html', context)


