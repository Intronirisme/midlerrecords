from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='midlerrecords'),
    path('contact', views.contact, name="contact")
]