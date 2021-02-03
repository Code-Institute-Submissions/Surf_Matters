from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
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

    blog = Blog.objects.get(slug=slug)
    post = get_object_or_404(Blog, slug=slug)
    comments = post.comments.filter()
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(
        request, 'blogs/blog_detail.html', {
            'blog': blog, 'post': post, 'comments': comments,
            'new_comment': new_comment, 'comment_form': comment_form})
