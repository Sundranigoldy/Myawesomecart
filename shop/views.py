from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
import json
from .models import Product, Contact, Orders, OrderUpdate  # to import all things from database

# Create your views here.


def index(request):
    products = Product.objects.all()  # fetching data from database..
    allProds = []
    # to diffn from category wise and id wise
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"]
            for item in catprods}  # catgeory in set compreehensation
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        # to calculate no of slide and ceil funct comes from math
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        # taking an range func so that i can use value in template func as it return generator
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}  # passing an template with name product
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method=="POST":
        # print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "shop/contact.html")

def search(request):
    return render(request, 'shop/search.html')


def productview(request, myid):
    #fetching the product using the id..
    product = Product.objects.filter(id=myid)

    return render(request, 'shop/productview.html', {'product':product[0]})
def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemjson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        address=request.POST.get('address', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zipcode=request.POST.get('zipcode', '')
        order = Orders(items_json=items_json, name=name, email=email, phone=phone, address=address, city=city,state=state, zipcode=zipcode)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed.")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id}) #sending parametre thank and id in script
    return render(request, 'shop/checkout.html')
def tracker(request):
    if request.method=="POST":
        orderid=request.POST.get('orderid', '')
        email=request.POST.get('email', '')
        # return HttpResponse(f"{orderid} and {email}")
        try:
            order = Orders.objects.filter(order_id=orderid, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderid)
                updates = []
                for items in update:
                    #update desc comes from checkout update.

                    #using json below and using json module, but was getting error becoz using item instead of items of json
                    updates.append({'text': items.update_desc, 'time': items.timestamp})
                    #just converting updates and itemsjson from orders
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("{}")
        except Exception as e:
            return HttpResponse("{}")
    return render(request, 'shop/TrackingStatus.html')