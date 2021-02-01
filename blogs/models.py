from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    opening = models.TextField(null=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
