from django.shortcuts import render, redirect

from product.models import Product

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
    context = {'products':products}
    template = 'product/product.html'
    if request.method == 'GET':
        return render(request,template,context)
    # POST
    name = request.POST.get('name')
    price = int(request.POST.get('price'))
    title = request.POST.get('title')
    Introduction = request.POST.get('Introduction')
    colour = request.POST.get('colour')
    smell = request.POST.get('smell')
    taste = request.POST.get('taste')
    After = request.POST.get('After')
    cask = request.POST.get('cask')
    
    product = Product()
    product.name=name
    product.price=price
    product.title=title
    product.Introduction=Introduction
    product.colour=colour
    product.smell=smell
    product.taste=taste
    product.After=After
    product.cask=cask
    product.save()
    return redirect('main:main')


