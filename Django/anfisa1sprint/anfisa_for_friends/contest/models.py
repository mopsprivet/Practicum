from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Contest(models.Model):
    title = models.CharField("Название", max_length=20)
    description = models.TextField("Описание", blank=True)
    comment = models.TextField("Комментарий", blank=True)
    price = models.IntegerField(
        "Цена",
        validators=[MinValueValidator(10), MaxValueValidator(100)],
        blank=True,
        null=True,
        help_text="Рекомендованная розничная цена"
    )
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка на конкурс"
        verbose_name_plural = "Заявки на конкурс"

    def __str__(self):
        return self.title
