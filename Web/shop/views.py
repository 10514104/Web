from django.shortcuts import render, redirect, get_object_or_404

from product.models import Product
from product.models import Shop


# Create your views here.

def shop(request):
    products = Product.objects.all()
    shops = Shop.objects.all()
    sub1 = 0
    sub = 0
    for x in shops:
        a=x.price * x.amount
        sub1+=a
        print(a)
    sub2=sub1+60
    
    context = {'products':products,'shops':shops,
               'sub':sub,'sub1':sub1,'sub2':sub2}
    return render(request, 'shop/shop.html',context)



def checkout(request):
    Delivery = request.GET.get('Delivery')
    payment = request.GET.get('payment')
    products = Product.objects.all()
    shops = Shop.objects.all()
    sub1 = 0
    sub = 0
    for x in shops:
        a=x.price * x.amount
        sub1+=a
        print(a)
    sub2=sub1+60
    context = {'products':products,'shops':shops,
               'payment':payment,'Delivery':Delivery,
               'sub':sub,'sub1':sub1,'sub2':sub2}
    return render(request, 'shop/checkout.html',context)



def order(request):
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    address = request.GET.get('address')
    remark = request.GET.get('remark')
    Delivery = request.GET.get('Delivery')
    payment = request.GET.get('payment')
    products = Product.objects.all()
    shops = Shop.objects.all()
    sub1 = 0
    sub = 0
    for x in shops:
        a=x.price * x.amount
        sub1+=a
        print(a)
    sub2=sub1+60
    context = {'products':products,'shops':shops,'name':name
               ,'phone':phone,'address':address,'remark':remark
               ,'Delivery':Delivery,'payment':payment,
               'sub':sub,'sub1':sub1,'sub2':sub2}
    return render(request, 'shop/order.html',context)



def shopDelete(request, shopId):
    if request.method == 'GET':
        return shop(request)
    # POST
    shopToDelete = get_object_or_404(Shop, id=shopId)
    shopToDelete.delete()
    return redirect('shop:shop')



def fin(request):
    if request.method == 'GET':
        return order(request)
    # POST
    shops = Shop.objects.all()
    for x in shops:
        x.delete()
    return redirect('shop:fin2')



def fin2(request):
    products = Product.objects.all()
    context = {'products':products }
    return render(request, 'shop/fin.html',context)






