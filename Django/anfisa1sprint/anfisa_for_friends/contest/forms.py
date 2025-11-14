import django.forms as forms


class ContestForm(forms.Form):
    title = forms.CharField(
        label='Название',
        max_length=20,
        required=True,
        widget=forms.TextInput(),
    )

    description = forms.CharField(
        label='Описание',
        required=True,
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}),
    )

    price = forms.IntegerField(
        label='Цена',
        required=True,
        min_value=10,
        max_value=100,
        help_text='Рекомендованная розничная цена',
        widget=forms.NumberInput(),
    )

    comment = forms.CharField(
        label='Комментарий',
        required=False,
        widget=forms.Textarea(attrs={'rows': 7, 'cols': 40}),
    )
