from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [ 
    path('', views.index, name='index'),
    path('contact/', contact_view, name='contact'),
]