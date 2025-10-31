from django.shortcuts import render


def index(request):
    template = 'homepage/index.html'
    # Запрос:
    ice_cream_list = IceCream.objects.all()
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template, context) 
