
from django.shortcuts import render, get_object_or_404
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

    return render(request, 'products/surf_lessons.html', context)


def product_details(request, product_id):
    """ A view to show individual products"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
