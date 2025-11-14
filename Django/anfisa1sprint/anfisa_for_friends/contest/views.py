from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContestForm
from .models import Contest

def proposal(request, pk=None):
    if pk is not None:
        instance = get_object_or_404(Contest, pk=pk)
    else:
        instance = None

    form = ContestForm(request.POST or None, instance=instance)

    form_is_valid = form.is_valid()

    if request.method == 'POST' and form_is_valid:
        form.save()  

    context = {
        'form': form,
        'form_is_valid': form_is_valid,
    }
    return render(request, 'contest/form.html', context)


def delete_proposal(request, pk):
    instance = get_object_or_404(Contest, pk=pk)
    form = ContestForm(instance=instance)

    if request.method == 'POST':
        instance.delete()
        return redirect('contest:list')

    return render(request, 'contest/form.html', {'form': form})


def proposal_list(request):
    contest_proposals = Contest.objects.order_by('id')
    return render(request, 'contest/contest_list.html', {'contest_proposals': contest_proposals})
