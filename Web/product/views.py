from django.shortcuts import render, redirect

from product.models import product
from django.contrib import messages
from product.forms import productForm


# Create your views here.


def product(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the article page
    '''
    # TODO: finish the code
    #products = product.objects.all()
    #context = {'products':products}
    template = 'product/product.html'
    if request.method == 'GET':
        return render(request,template, {'productForm':productForm()})
    # POST
    ProductForm = productForm(request.POST)
    if not ProductForm.is_valid():
        return render(request, template, {'productForm':ProductForm})
    ProductForm.save()
    messages.success(request, '產品已新增')
    return redirect('main:main')


