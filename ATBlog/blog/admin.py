from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Post, Comment
# Register your models here.

# for showing posts in admin page
admin.site.register(Post)

admin.site.register(Comment)
