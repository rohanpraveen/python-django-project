#mapping urls to views
from django.urls import path
from . import views

urlpatterns  = [ 
 path('hello/',views.say_hello)
]