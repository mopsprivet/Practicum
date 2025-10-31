from django.db.models import Q 
from django.shortcuts import render 

from ice_cream.models import IceCream 

def index(request):
    template = 'homepage/index.html'
    # Запрос: # Верни только те объекты, у которых в поле is_on_main указано True: 
    ice_cream_list = IceCream.objects.values('id', 'title', 'description'
        ).filter(
            is_published=True, is_on_main=True
        ).order_by('title')[1:4] 
    
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template, context) 
