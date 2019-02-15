from django.shortcuts import render, redirect

from django.contrib import messages

from .forms import PostForm

from administration.models import Project

from .models import Post

from .utils import create_post, get_used_codes, get_unused_codes, ApplicableCode

# Create your views here.
def homepage_view(request):
    context = {}
    return render(request, 'posting/homepage.html', context)

def remove_coupon_view(request, pk):
    try:
        ApplicableCode.objects.get(pk=pk).delete()
    except:
        messages.error(request, "Error, you cannot remove this code from this post!")
    return redirect('administration:homepage')

def add_post_view(request, pk):
    if request.method == "GET":
        context = {
        'form': PostForm(),
        'project': Project.objects.get(pk=pk)
        }
        return render(request, 'posting/post_details.html', context)

    form = PostForm(request.POST)
    if not form.is_valid():
        context = {
        'form': form,
        'project': Project.objects.get(pk=pk)
        }
        return render(request, 'posting/post_details.html', context)
    create_post(form.cleaned_data, pk)
    return redirect('administration:homepage')

def update_post_view(request, pk):
    if request.method == "GET":
        context = {
        'form': PostForm(),
        'project': Project.objects.get(pk=pk)
        }
        return render(request, 'posting/post_details.html', context)

    form = PostForm(request.POST)
    if not form.is_valid():
        context = {
        'form': form,
        'project': Project.objects.get(pk=pk)
        }
        return render(request, 'posting/post_details.html', context)
    create_post(form.cleaned_data, pk)
    return redirect('administration:homepage')

def add_codes_to_post_view(request, pk):
    context = {
        'unused_codes': get_unused_codes(pk),
        'used_codes': get_used_codes(pk),
        "post": Post.objects.get(pk=pk)
    }
    return render(request, 'posting/manage_codes.html', context)
