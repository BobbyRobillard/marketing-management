from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.edit import DeleteView, UpdateView, CreateView

from marketing.utils import get_class_based_default_context

from .models import Poll
from .forms import AddPollForm


# Create your views here.
def homepage_view(request):
    context = {
        "polls": Poll.objects.all(),
        "form": AddPollForm()
    }
    return render(request, 'voting/voting.html', context)


def add_poll(request):
    context = {}
    if request.method == "POST":
        form = AddPollForm(request.POST)
        if form.is_valid():
            form.instance.creator = request.user
            form.save()
            return redirect('voting:homepage')
        else:
            context['form'] = form
            context['polls'] = Poll.objects.all()
    return render(request, 'voting/voting.html', context)
