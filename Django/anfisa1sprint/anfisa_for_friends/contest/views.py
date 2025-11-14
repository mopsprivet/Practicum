from django.shortcuts import render
from .forms import ContestForm


def proposal(request):
    if request.GET:
        form = ContestForm(request.GET)
        if form.is_valid():
            pass
    else:
        form = ContestForm()
    return render(request, 'contest/form.html', {'form': form})
