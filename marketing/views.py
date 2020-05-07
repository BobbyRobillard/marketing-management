from django.shortcuts import render

from .utils import get_projects, get_tasks, get_default_context


def homepage_view(request):
    context = get_default_context(request.user)
    return render(request, 'marketing/homepage.html', context)


def tasks_view(request, status):
    context = get_default_context(request.user)
    context_tasks = get_tasks(request.user, status)
    return render(request, 'marketing/tasks.html', context)
