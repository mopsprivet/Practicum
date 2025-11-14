from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Contest  

class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ['title', 'description', 'price', 'comment']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'price': 'Цена',
            'comment': 'Комментарий',
        }
        help_texts = {
            'price': 'Рекомендованная розничная цена',
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': '22', 'rows': '5'}),
            'comment': forms.Textarea(attrs={'cols': '22', 'rows': '5'}),
        }
