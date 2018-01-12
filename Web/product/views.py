from django.shortcuts import render, redirect

from product.models import Product
from product.forms import ProductForm

# Create your views here.


def product(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the article page
    '''
    # TODO: finish the code
    products = Product.objects.all()
    context = {'products':products,'productForm':ProductForm()}
    template = 'product/product.html'
    if request.method == 'GET':
        return render(request,template,context)
    # POST
    productForm = ProductForm(request.POST)
    if not productForm.is_valid():
        return render(request, template, {'productForm':productForm})
    productForm.save()
    return redirect('main:main')


