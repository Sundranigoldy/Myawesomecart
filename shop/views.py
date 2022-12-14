from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Product #to import all things from database

# Create your views here.
def index(request):
    products= Product.objects.all() # fetching data from database..
    allProds=[]
    catprods= Product.objects.values('category', 'id') # to diffn from category wise and id wise
    cats= {item["category"] for item in catprods} #catgeory in set compreehensation
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4)) #to calculate no of slide and ceil funct comes from math
        allProds.append([prod, range(1, nSlides), nSlides]) #taking an range func so that i can use value in template func as it return generator

    params={'allProds':allProds } #passing an template with name product
    return render(request,"shop/index.html", params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse('We are at contact')         

def tracker(request):
    return HttpResponse('We are at tracker')

def search(request):
    return HttpResponse('We are at search')

def productview(request):
    return HttpResponse('We are at productview')

def checkout(request):
    return HttpResponse('We are at checkout')
