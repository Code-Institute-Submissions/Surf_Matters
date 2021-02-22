from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Subcategory, Category
from .forms import AmendProductsForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    lessons_category = Category.objects.filter(
        name__icontains="Lesson").first()

    if request.GET.get('category'):
        is_products = request.GET.get('category') != lessons_category.name  # reused variable at the bottom
        products = Product.objects.filter(~Q(category__name__icontains='Lesson')) if is_products else Product.objects.filter(Q(category__name__icontains='Lesson'))
    else:
        # Search
        is_products = True
        products = Product.objects.all()

    query = None
    categories = None
    subcategories = None
    sort = None
    direction = None

    if request.GET:
        # Check if sort in request
        if 'sort' in request.GET:
            # Set sort to these variables
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                # Annotate currwent list with a new field
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'subcategory':
                sortkey == 'subcategory__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                # Check if direction is descending
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'subcategory' in request.GET:
            subcategories = request.GET['subcategory']
            products = products.filter(subcategory__name__exact=subcategories)
            subcategories = Subcategory.objects.filter(name__in=subcategories)

        if 'category' in request.GET:
            categories = request.GET['category']
            products = products.filter(category__name__exact=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search citeria entered!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        # Used for deciding whether or not to render the product filtering buttons
        'is_products': is_products,
        # This was moved from the FE to the BE because it's business logic
        'page_h1': 'Products' if is_products else 'Lessons',
        'products': products,
        'search_term': query,
        'current_subcategories': subcategories,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to show individual products"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """Add a new product to the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only administrators can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AmendProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Your product has been added!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(
                request, 'Could not add that product, please try again!')
    else:
        form = AmendProductsForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only administrators can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = AmendProductsForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product has been updated!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(
                request, 'Could not update that product, please try again.')
    else:
        form = AmendProductsForm(instance=product)
    messages.info(request, f'You are currently editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only administrators can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
