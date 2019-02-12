from django.shortcuts import render, redirect

from .forms import PostForm

from administration.models import Project

from .utils import create_post

# Create your views here.
def homepage_view(request):
    context = {}
    return render(request, 'posting/homepage.html', context)

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
