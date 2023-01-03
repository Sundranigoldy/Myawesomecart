from django.contrib import admin
from django.urls import path
from . import views
app_name = "shop"
urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("tracker", views.tracker, name="TrackingStatus"),
    path("search", views.search, name="Search"),
    path('product/<int:myid>', views.productview, name="productview"),
    path("checkout", views.checkout, name="checkout"),
]