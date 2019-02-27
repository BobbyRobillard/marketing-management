from django.shortcuts import render, redirect

from django.contrib import messages

from django.http import JsonResponse

from django.views.generic.edit import DeleteView, UpdateView, CreateView

from django.urls import reverse_lazy

from .forms import PostForm, PostLocationForm

from administration.models import Project

from .models import Post, PostLocation

from .utils import create_post, get_used_codes, get_unused_codes

import json

# Create your views here.
def homepage_view(request):
    context = {}
    return render(request, 'posting/homepage.html', context)

def remove_coupon_view(request, pk):
    # try:
    #     c = ApplicableCode.objects.get(pk=pk)
    #     p = c.post
    #     c.delete()
    #     messages.success(request, "Coupon unapplied")
    #     return add_codes_to_post_view(request, p.pk)
    # except:
    #     messages.error(request, "Error, you cannot remove this code from this post!")
    return redirect('administration:homepage')

class AddPostLocationView(CreateView):
    model = PostLocation
    template_name = 'posting/post_location_form.html'
    form_class = PostLocationForm

    def get_success_url(self):
        return reverse_lazy('posting:update_post', kwargs={'pk': self.kwargs.get('pk')})

#creates a new post
class AddPostView(CreateView):
    success_url = reverse_lazy('administration:homepage')
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('administration:view_project', kwargs={'pk': Post.objects.get(pk=self.kwargs.get('pk')).project.pk})

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'posting/post_detail.html'
    form_class = PostForm
    success_url = reverse_lazy('administration:homepage')

    def get_context_data(self, **kwargs):
        context = super(UpdatePostView, self).get_context_data(**kwargs)
        context['locations'] = PostLocation.objects.filter(post=Post.objects.get(pk=self.kwargs.get('pk')))
        return context

def add_codes_to_post_view(request, pk):
    context = {
        'unused_codes': get_unused_codes(pk),
        'used_codes': get_used_codes(pk),
        "post": Post.objects.get(pk=pk)
    }
    return render(request, 'posting/manage_codes.html', context)

def use_codes_view(request, pk):
    # post = Post.objects.get(pk=pk)
    # for code in json.loads(request.body.decode("utf-8"))['codes_to_apply']:
    #     if not ApplicableCode.objects.filter(code=code, post=post).exists():
    #         ApplicableCode.objects.create(code=code, post=post)
    #     else:
    #         messages.error(request, "Code already is use for this post.")
    return JsonResponse({})
