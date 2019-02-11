from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from django.contrib import messages
from django.shortcuts import render, redirect

#-------------------------------------------------------------------------------
# Page Views
#-------------------------------------------------------------------------------
@login_required
def homepage_view(request):
    context = {}
    return redirect('administration:homepage')
