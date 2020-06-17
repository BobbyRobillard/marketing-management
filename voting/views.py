from django.shortcuts import render, redirect

from django.core.mail import send_mail

from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from django.views.generic.edit import DeleteView, UpdateView, CreateView

from marketing.utils import get_class_based_default_context

from .models import Poll, Vote
from .forms import AddPollForm


@login_required
# Create your views here.
def homepage_view(request):
    context = {
        "polls": Poll.objects.all(),
        "form": AddPollForm()
    }
    return render(request, 'voting/voting.html', context)


@login_required
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


@login_required
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


@login_required
def poll_alert(request, pk):
    try:
        poll = Poll.objects.get(pk=pk)
        send_mail(
            'Vote Now In Marketing Management',
            '{0} has requested you vote on the poll: {1}. Vote now: http://mm.techandmech.com/voting'.format(request.user, str(poll)),
            'webmaster@mm.techandmech.com',
            User.objects.all().values_list('email', flat=True),
            fail_silently=False,
        )
        messages.success(request, 'Users have been notified to vote on the poll!')
    except Exception as e:
        print(str(e))
    return redirect('voting:homepage')


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
