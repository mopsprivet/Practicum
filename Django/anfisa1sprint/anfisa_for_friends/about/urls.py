from django.urls import path
from .views import Description

app_name = 'about'

urlpatterns = [
    path('', Description.as_view(), name='description'),
]
