from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
   
    allProduct = []
    catprods = Product.objects.values('category', 'id') #<QuerySet [{'category': 'Shoes', 'id': 8}, {'category': 'Shoes', 'id': 9}]>
    
    cats = {item['category'] for item in catprods} #cats {'Shoes', 'Earphon', 'Earphone'}
    
    for cat in cats:
        products = Product.objects.filter(category=cat)
        print(products)
        n = len(products)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProduct.append([products, range(1, nSlides)]) #, nSlides
    context={"allproduct":allProduct}
    print("all product",allProduct)
    return render(request,'home.html',context)
def about(request):
    return HttpResponse("Its about")

def contact(request):
    return HttpResponse("Hello contact")
def tracker(request):
    return HttpResponse("Hello tracker")
def checkout(request):
    return HttpResponse("Hello checkout")
def search(request):
    return HttpResponse("Hello search")
def product(request,id):
    prod=Product.objects.filter(id=id).first()
    context={"product":prod}
    print(product)
    return render(request,'product.html',context)