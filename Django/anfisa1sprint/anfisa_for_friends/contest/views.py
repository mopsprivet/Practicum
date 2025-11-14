from django.shortcuts import render
from .forms import ContestForm


def proposal_create(request):
    form = ContestForm()
    return render(request, 'contest/form.html', {'form': form})


def accepted(request):
    return render(request, 'contest/proposal_accepted.html')