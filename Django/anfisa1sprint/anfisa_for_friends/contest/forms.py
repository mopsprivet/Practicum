from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Contest

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}

class ContestForm(forms.ModelForm):

    def clean(self):
        super().clean()
        title = self.cleaned_data['title']
        if f'{title}' in BEATLES:
            # Отправляем письмо, если кто-то представляется 
            # именем одного из участников Beatles.
            send_mail(
                subject='Another Beatles ice cream',
                message=f'{title} ожил и пытается быть мороженым!',
                from_email='contest_form@acme.not',
                recipient_list=['admin@acme.not'],
                fail_silently=True,
            )
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее название мороженого!'
            ) 

    class Meta:
        model = Contest
        fields = '__all__'
        widgets = {
            'description': forms.Textarea({'cols': '22', 'rows': '5'}),
            'comment': forms.Textarea({'cols': '22', 'rows': '5'}),
        }