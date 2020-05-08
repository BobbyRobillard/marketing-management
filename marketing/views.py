from django.contrib import messages

from django.http import JsonResponse

from django.shortcuts import render, redirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string

from django.views.generic.edit import DeleteView, UpdateView, CreateView

from .models import TYPE_CHOICES, Project, Resource
from .utils import (get_projects, get_tasks, get_default_context, get_locations,
                    get_platforms, get_sample_posts, get_live_posts, get_resources,
                    get_class_based_default_context, set_current_project, get_current_project)


def homepage_view(request):
    context = get_default_context(request.user)
    return render(request, 'marketing/homepage.html', context)


@login_required
def set_current_project_view(request, pk):
    set_current_project(request.user, pk)
    messages.success(request, "Current project changed to: {0}".format(
        get_current_project(request.user)
    ))
    return redirect('marketing:homepage')


@method_decorator(login_required, name="dispatch")
class CreateProjectView(CreateView):
    model = Project
    fields = "__all__"
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProjectView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        return get_class_based_default_context(
            super().get_context_data(**kwargs),
            self.request.user
        )


def tasks_view(request, status):
    context = get_default_context(request.user)
    context['tasks'] = get_tasks(request.user, status)
    return render(request, 'marketing/tasks.html', context)


def locations_view(request):
    context = get_default_context(request.user)
    context['locations'] = get_locations(request.user)
    return render(request, 'marketing/locations.html', context)


def sample_posts_view(request):
    context = get_default_context(request.user)
    context['sample_posts'] = get_sample_posts(request.user)
    return render(request, 'marketing/sample_posts.html', context)


def live_posts_view(request):
    context = get_default_context(request.user)
    context['live_posts'] = get_live_posts(request.user)
    return render(request, 'marketing/live_posts.html', context)


@method_decorator(login_required, name="dispatch")
class CreateResourceView(CreateView):
    model = Resource
    fields = "__all__"
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateResourceView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        return get_class_based_default_context(
            super().get_context_data(**kwargs),
            self.request.user
        )


def resources_view(request):
    context = get_default_context(request.user)
    context['resources'] = get_resources()
    context['types'] = [type[1] for type in TYPE_CHOICES]
    return render(request, 'marketing/resources.html', context)
