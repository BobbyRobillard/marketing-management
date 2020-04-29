from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def homepage_view(request):
    context = {
    }
    return render(request, "website/homepage.html", context)
