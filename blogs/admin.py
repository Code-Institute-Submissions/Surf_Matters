from django.contrib import admin
from .models import Blog, Comment

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'author',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'email',
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
