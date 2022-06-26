from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'body', 'publish', 'status']

admin.site.register(Post, PostAdmin)
