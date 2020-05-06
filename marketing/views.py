from django.shortcuts import render

from .utils import get_projects


# Create your views here.
def homepage_view(request):
    context = {
        "projects": get_projects(request.user)
    }
    return render(request, 'marketing/homepage.html', context)
