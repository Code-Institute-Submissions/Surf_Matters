from django.shortcuts import render
from .models import Product, SurfLesson


def all_products(request):
    """ A view to show all products"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def surf_lessons(request):
    """ A view to show all products"""

    surf_lessons = SurfLesson.objects.all()

    context = {
        'surf_lessons': surf_lessons,
    }

    return render(request, 'surf_lessons/surf_lessons.html', context)
