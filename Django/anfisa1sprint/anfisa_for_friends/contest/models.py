from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models 
from django.contrib.auth import get_user_model 

User = get_user_model()

class Contest(models.Model):
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )
    title = models.CharField(verbose_name='Название', max_length=20)
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(
        verbose_name='Цена',
        validators=[MinValueValidator(10), MaxValueValidator(100)],
        help_text='Рекомендованная розничная цена',
    )
    comment = models.TextField(verbose_name='Комментарий', blank=True)