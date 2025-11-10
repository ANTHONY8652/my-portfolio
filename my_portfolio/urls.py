from django.urls import path
from . import views
from .views import contact_view, download_cv

urlpatterns = [ 
    path('', views.index, name='index'),
    path('contact/', contact_view, name='contact'),
    path('download-cv/', download_cv, name='download_cv'),
]