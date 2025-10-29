from django.db import models


# Создайте абстрактную PublishedModel модель тут 
class PublishedModel(models.Model): 
    is_published = models.BooleanField(default=True) 

    class Meta: 
        abstract = True 

