from .views import index, about, my_contacts
from django.urls import path

urlpatterns = [
    path('my_hobby', index, name='my_hobby'),
    path('about_me', about, name='about_me'),
    path('my_contacts', my_contacts, name='my_contact')
]