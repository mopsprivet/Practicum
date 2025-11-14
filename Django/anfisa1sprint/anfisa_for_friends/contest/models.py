from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Contest(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(100)])
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.title
