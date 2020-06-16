from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from django.views.generic.edit import DeleteView, UpdateView, CreateView

from marketing.utils import get_class_based_default_context

from .models import Poll, Vote
from .forms import AddPollForm


# Create your views here.
def homepage_view(request):
    context = {
        "polls": Poll.objects.all(),
        "form": AddPollForm()
    }
    return render(request, 'voting/voting.html', context)


def vote_view(request, result, poll):
    try:
        v = Vote.objects.get(poll__pk=poll, user=request.user)
        v.is_yes = bool(int(result))
        v.save()
        messages.success(request, 'Your vote has been changed!')
    except Exception as e:
        Vote.objects.create(
            user=request.user, poll=Poll.objects.get(pk=poll), is_yes=bool(result)
        )
        messages.success(request, 'Your vote has been recorded!')
    return redirect('voting:homepage')


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


@method_decorator(login_required, name="dispatch")
class DeletePollView(DeleteView):
    model = Poll
    success_url = "/voting"

    def get_context_data(self, **kwargs):
        return get_class_based_default_context(
            super().get_context_data(**kwargs),
            self.request.user
        )

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Poll deleted!")
        return super(DeletePollView, self).delete(*args, **kwargs)
