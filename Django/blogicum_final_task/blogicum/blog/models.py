from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model() 

class PublishedCreatedModel(models.Model): 
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        abstract = True 


class Category(PublishedCreatedModel): 
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True) 


class Location(PublishedCreatedModel): 
    name = models.CharField(max_length=256)


class Post(PublishedCreatedModel): 
    title = models.CharField(max_length=256) 
    text = models.TextField()
    pub_date = models.DateTimeField() 
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    ) 
    location = models.ForeignKey(
        Location, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True 
    ) 
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True 
    ) 
