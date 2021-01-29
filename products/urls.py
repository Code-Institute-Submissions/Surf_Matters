from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('', views.surf_lessons, name='surf_lessons'),
]
