from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('surf_lessons', views.surf_lessons, name='surf_lessons'),
    path('<int:product_id>/', views.product_details, name='product_details'),
]
