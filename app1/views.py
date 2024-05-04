from django.shortcuts import render, redirect
from .models import Product,Category,ProductVarient
from .forms import ProductForm

# Create your views here.
def home(request):
    
    return render(request,'home.html')

def productadd(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render (request,'productadd.html', {'form':form})

def product_list(request):
    products = Product.objects.all()
    return render(request,'product_list.html', {'products':products})


def product_view(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request,'product_view.html', {'product':product})

def category_list(request):
    categories=Category.objects.all()
    return render(request,'category_list.html',{'categories':categories})

def category_product(request,category_id):
    categorysid=Category.objects.get(id=category_id)
    product=Product.objects.filter(category=categorysid)
    return render(request,'category_product.html',{'category':categorysid, 'product':product})

def product_with_product_varient(request,product_id):
    productsid=Product.objects.get(id=product_id)
    productvarient=ProductVarient.objects.filter(product=productsid)
    return render(request,'product_with_product_varient.html',{'product':productsid,'productvarient':productvarient})
    
