from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

from .models import Project
from posting.models import Post, Topic, PostLocation

from .utils import get_all_projects

@login_required
def homepage_view(request):
    context = {
    "projects" : get_all_projects().order_by('name')
    }
    return render(request, 'administration/homepage.html', context)

class ViewProjectView(LoginRequiredMixin, DetailView):
    model = Project

class ViewProjectPosts(LoginRequiredMixin, TemplateView):
    template_name = 'administration/project_detail.html'

    def get_context_data(self, **kwargs):
        project = Project.objects.get(pk=self.kwargs.get('project'))
        topic = Topic.objects.get(pk=self.kwargs.get('topic'))
        context = {
            'project': project,
            'topic': topic,
            'posts': Post.objects.filter(project=project, topic=topic)
        }
        return context

class ViewPostLocations(LoginRequiredMixin, TemplateView):
    template_name = 'administration/project_detail.html'

    def get_context_data(self, **kwagrs):
        project = Project.objects.get(pk=self.kwargs.get('project'))
        topic = Topic.objects.get(pk=self.kwargs.get('topic'))
        post = Post.objects.get(pk=self.kwargs.get('post'))
        context = {
            'project': project,
            'topic': topic,
            'post': post
        }
        return context


class UpdateProjectView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'administration/project_form.html'
    fields = "__all__"
    success_url = reverse_lazy('administration:homepage')

class AddProjectView(LoginRequiredMixin, CreateView):
    model = Project
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy('administration:homepage')

@login_required
def delete_project(request, pk):
    try:
        Project.objects.get(pk=pk).delete()
        messages.success(request, "Project Deleted.")
    except Exception as e:
        pass
        messages.error(request, "Could not delete project.")
    return redirect('administration:homepage')

def financial_summary_view(request, pk):
    context = {
    "project": Project.objects.get(pk=pk)
    }
    return render(request, 'administration/financial_summary.html', context)
