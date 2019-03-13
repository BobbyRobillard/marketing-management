from django.shortcuts import render, redirect, reverse

from django.contrib import messages

from django.http import JsonResponse

from django.views.generic.edit import DeleteView, UpdateView, CreateView

from django.urls import reverse_lazy

from .forms import PostForm, PostLocationForm

from administration.models import Project

from .models import Post, PostLocation, Topic

from .utils import create_post, get_used_codes, get_unused_codes

import json

# Create your views here.
def homepage_view(request):
    context = {}
    return render(request, 'posting/homepage.html', context)

def remove_post_location_view(request, pk):
    try:
        p = PostLocation.objects.get(pk=pk)
        post_pk = p.post.pk
        p.delete()
        messages.success(request, "Post location deleted.")
    except:
        pass
    return redirect('administration:homepage')

class AddPostLocationView(CreateView):
    model = PostLocation
    template_name = 'posting/post_location_form.html'
    form_class = PostLocationForm

    def get_success_url(self):
        return reverse_lazy('posting:update_post', kwargs={'pk': self.kwargs.get('pk')})

    def get_initial(self, **kwargs):
        initial = super(AddPostLocationView, self).get_initial(**kwargs)
        post = Post.objects.get(pk=self.kwargs.get('pk'))
        initial['post'] = post
        return initial

#creates a new post
class AddPostView(CreateView):
    model = Post
    form_class = PostForm

    def get_initial(self, **kwargs):
        initial = super(AddPostView, self).get_initial(**kwargs)
        project = Project.objects.get(pk=self.kwargs.get('project'))
        topic = Topic.objects.get(pk=self.kwargs.get('topic'))
        initial['project'] = project
        initial['topic'] = topic
        return initial

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'posting/post_detail.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super(UpdatePostView, self).get_context_data(**kwargs)
        context['locations'] = PostLocation.objects.filter(post=Post.objects.get(pk=self.kwargs.get('pk')))
        return context

class AddTopicView(CreateView):
    model = Topic
    fields = '__all__'

    def get_initial(self, **kwargs):
        initial = super(AddTopicView, self).get_initial(**kwargs)
        initial['project'] = Project.objects.get(pk=self.kwargs.get('pk'))
        return initial

def add_codes_to_post_view(request, pk):
    context = {
        'unused_codes': get_unused_codes(pk),
        'used_codes': get_used_codes(pk),
        "post": Post.objects.get(pk=pk)
    }
    return render(request, 'posting/manage_codes.html', context)

def delete_topic(request, pk):
    try:
        t = Topic.objects.get(pk=pk)
        p = t.project
        t.delete()
        return redirect('administration:view_project', pk=p.pk)
    except Exception as e:
        print(str(e))

    return redirect('website:homepage')

def delete_post(request, pk):
    try:
        p = Post.objects.get(pk=pk)
        topic = p.topic
        p.delete()
        return redirect('administration:view_project_posts', project=topic.project.pk, topic=topic.pk)
    except Exception as e:
        print(str(e))
    return home('website:homepage')

def use_codes_view(request, pk):
    # post = Post.objects.get(pk=pk)
    # for code in json.loads(request.body.decode("utf-8"))['codes_to_apply']:
    #     if not ApplicableCode.objects.filter(code=code, post=post).exists():
    #         ApplicableCode.objects.create(code=code, post=post)
    #     else:
    #         messages.error(request, "Code already is use for this post.")
    return JsonResponse({})
