from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blogs'),
    path('<slug:slug>/', views.blog_details, name='blog_details'),
]
