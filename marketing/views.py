from django.shortcuts import render

from .models import TYPE_CHOICES
from .utils import (get_projects, get_tasks, get_default_context, get_locations,
                    get_platforms, get_sample_posts, get_live_posts, get_resources)


def homepage_view(request):
    context = get_default_context(request.user)
    return render(request, 'marketing/homepage.html', context)


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


def resources_view(request):
    context = get_default_context(request.user)
    context['resources'] = get_resources(request.user)
    context['types'] = [type[1] for type in TYPE_CHOICES]
    return render(request, 'marketing/resources.html', context)
