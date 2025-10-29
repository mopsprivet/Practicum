from django.db import models

from core.models import PublishedModel

class Category(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)

class Wrapper(PublishedModel): 
    title = models.CharField(max_length=256) 

class Topping(PublishedModel): 
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)

class IceCream(PublishedModel): 
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_on_main = models.BooleanField(default=False)
    wrapper = models.OneToOneField(Wrapper, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
