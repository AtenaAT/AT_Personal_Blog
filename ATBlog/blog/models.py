from django.db import models
from django.contrib.auth.models import User

# post model for db

# for publish the post or save it as draft in admin pagemun
status = ((0, "Draft",),(1, "Publish"))

class Post(models.Model):
    title =models.CharField(max_length=120) 
    description =models.TextField()
    slug =models.SlugField(max_length=120)
    auther =models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    time_created =models.DateTimeField(auto_now_add=True)
    time_updated =models.DateTimeField(auto_now=True)
    status =models.IntegerField(choices=status)

    #show better
    def __str__(self):
        return self.title

    #tartibe post haye namayesh dade shode
    class Ordering_Posts:
        order = ["-time_created"]

 


#comment for each posts
class Comment(models.Model):
    name =models.CharField(max_length=120)
    email =models.EmailField()
    content =models.TextField()
    time_created =models.DateTimeField()
    post =models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    #show better
    def __str__(self):
        return "comment {}  by {}".format(self.content, self.name)
    
     #tartibe comment haye namayesh dade shode
    class Ordering_Comment:
        order = ["-time_created"]




