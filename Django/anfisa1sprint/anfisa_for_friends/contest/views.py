from django.shortcuts import render
from .forms import ContestForm
from .models import Contest

def proposal(request):
    form = ContestForm(request.POST or None)
    saved_contest = None

    form_is_valid = form.is_valid()

    if request.method == 'POST' and form_is_valid:
        saved_contest = form.save()  
    context = {
        'form': form,
        'saved_contest': saved_contest,
        'form_is_valid': form_is_valid,
    }
    return render(request, 'contest/form.html', context)


def proposal_list(request):
    contests = Contest.objects.all().order_by('id')
    return render(request, 'contest/contest_list.html', {'contests': contests})
