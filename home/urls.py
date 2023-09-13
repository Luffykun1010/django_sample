from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('booking',views.booking,name='booking'),
    path('department',views.department,name='department'),
    path('contact',views.contact,name='contact'),
    path('doctor',views.doctor,name='doctor'),
    path('drhafeez',views.hafeez,name='drhafeez'),
    path('gynecologist',views.gynecologist,name='gynecologist'),
    path('surgeon',views.surgeon,name='surgeon'),
] 