from django.shortcuts import render
from .models import Blog


def blog(request):
    """ A view to return the blog page """

    blogs = Blog.objects.all().order_by('date')

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/blog.html', context)


def blog_details(request, slug):
    """ A view to show individual blogs"""

    # return HttpResponse(slug)

    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})
