from django.shortcuts import render

from product.models import product


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    products = product.objects.all()
    context = {'products':products}
    return render(request, 'main/main.html',context)
