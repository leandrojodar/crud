from math import prod
from django.shortcuts import redirect, render
from product.models import Product

def list_products(self):
    products = Product.objects.all()
    return render(self, 'index.html', {'products':products})

def create_product(request):
    if request.method == 'POST':
        product = Product()
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.save()
        return redirect('/productos/')
    
def update(request, id):
    product = Product.objects.get(id=id)
    product.name = request.POST['name']
    product.price = request.POST['price']
    product.save()
    return redirect('/productos/')

def delete(id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/productos')

def hijo1(request):
    return render(request, 'hijo1.html')

def hijo2(request):
    return render(request, 'hijo2.html')