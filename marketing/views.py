from django.contrib import messages

from django.http import JsonResponse

from django.shortcuts import render, redirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string

from django.views.generic.edit import DeleteView, UpdateView, CreateView

from .models import TYPE_CHOICES, Project, Resource, Location, SamplePost, Task
from .utils import (get_projects, get_tasks, get_default_context, get_locations,
                    get_platforms, get_sample_posts, get_live_posts, get_resources,
                    get_class_based_default_context, set_current_project, get_current_project)


def homepage_view(request):
    context = get_default_context(request.user)
    return render(request, 'marketing/homepage.html', context)


# ------------------------------------------------------------------------------
# PROJECTS
# ------------------------------------------------------------------------------


@login_required
def set_current_project_view(request, pk):
    set_current_project(request.user, pk)
    messages.success(request, "Current project changed to: {0}".format(
        get_current_project(request.user)
    ))
    return redirect('marketing:homepage')


@method_decorator(login_required, name="dispatch")
class CreateProjectView(CreateView):
    model = Project
    fields = "__all__"
    success_url = "/"

    def get_context_data(self, **kwargs):
        return get_class_based_default_context(
            super().get_context_data(**kwargs),
            self.request.user
        )


# ------------------------------------------------------------------------------
# TASKS
# ------------------------------------------------------------------------------
@login_required
def tasks_view(request):
    context = get_default_context(request.user)
    context['tasks'] = get_tasks(request.user)
    return render(request, 'marketing/tasks.html', context)


@login_required
def mark_task_complete_view(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.completed = True
        task.save()
        messages.success(request, "{0} Marked As Completed".format(str(task)))
    except Exception as e:
        print(str(e))
    return redirect('marketing:tasks')


@method_decorator(login_required, name="dispatch")
class CreatePostingTaskView(CreateView):
    model = Task
    fields = (
        'create_post', 'assigned_to', 'locations',
        'sample_post', 'due_date',
    )
    success_url = "/"

    def get_context_data(self, **kwargs):
        return get_class_based_default_context(
            super().get_context_data(**kwargs),
            self.request.user
        )

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(CreatePostingTaskView, self).form_valid(form)


@method_decorator(login_required, name="dispatch")
class DeleteTaskView(DeleteView):
    model = Task
    success_url = "/"

    def get_context_data(self, **kwargs):
        return get_class_based_default_context(
            super().get_context_data(**kwargs),
            self.request.user
        )

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Task Unassigned!")
        return super(DeleteTaskView, self).delete(*args, **kwargs)
# ------------------------------------------------------------------------------
# LOCATIONS
# ------------------------------------------------------------------------------


@method_decorator(login_required, name="dispatch")
class CreateLocationView(CreateView):
    model = Location
    fields = "__all__"
    success_url = "/"

    def get_context_data(self, **kwargs):
        return get_class_based_default_context(
            super().get_context_data(**kwargs),
            self.request.user
        )


@method_decorator(login_required, name="dispatch")
class DeleteLocationView(DeleteView):
    model = Location
    success_url = "/"

    def get_context_data(self, **kwargs):
        return get_class_based_default_context(
            super().get_context_data(**kwargs),
            self.request.user
        )

    def delete(self, *args, **kwargs):
        # # Change user's current profile, only if it is the one being deleted
        # try:
        #     settings = get_settings(self.request.user)
        #     if settings.current_profile.pk == object.pk:
        #         profile = get_profiles(settings.user).exclude(pk=object.pk).first()
        #         settings.current_profile = profile
        #         settings.save()
        # except Exception as outer_error:
        #     messages.error(
        #         self.request, "You have no profiles to set as your current profile."
        #     )

        messages.success(self.request, "Location Deleted!")
        return super(DeleteLocationView, self).delete(*args, **kwargs)


def locations_view(request):
    context = get_default_context(request.user)
    context['locations'] = get_locations(request.user)
    return render(request, 'marketing/locations.html', context)

# ------------------------------------------------------------------------------
# SAMPLE POSTS
# ------------------------------------------------------------------------------


def sample_posts_view(request):
    context = get_default_context(request.user)
    context['sample_posts'] = get_sample_posts(request.user)
    return render(request, 'marketing/sample_posts.html', context)


@method_decorator(login_required, name="dispatch")
class CreateSamplePostView(CreateView):
    model = SamplePost
    fields = ('caption','title','tags','resources',)
    success_url = "/"

    def get_context_data(self, **kwargs):
        return get_class_based_default_context(
            super().get_context_data(**kwargs),
            self.request.user
        )


@method_decorator(login_required, name="dispatch")
class DeleteSamplePostView(DeleteView):
    model = SamplePost
    fields = "__all__"
    success_url = "/"

    def get_context_data(self, **kwargs):
        return get_class_based_default_context(
            super().get_context_data(**kwargs),
            self.request.user
        )

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Sample Post Deleted!")
        return super(DeleteSamplePostView, self).delete(*args, **kwargs)

# ------------------------------------------------------------------------------
# LIVE POSTS
# ------------------------------------------------------------------------------

def live_posts_view(request):
    context = get_default_context(request.user)
    context['live_posts'] = get_live_posts(request.user)
    return render(request, 'marketing/live_posts.html', context)


@method_decorator(login_required, name="dispatch")
class CreateResourceView(CreateView):
    model = Resource
    fields = "__all__"
    success_url = "/"

    def get_context_data(self, **kwargs):
        return get_class_based_default_context(
            super().get_context_data(**kwargs),
            self.request.user
        )


@method_decorator(login_required, name="dispatch")
class DeleteResourceView(DeleteView):
    model = Resource
    fields = "__all__"
    success_url = "/"

    def get_context_data(self, **kwargs):
        return get_class_based_default_context(
            super().get_context_data(**kwargs),
            self.request.user
        )

    def delete(self, *args, **kwargs):
        # # Change user's current profile, only if it is the one being deleted
        # try:
        #     settings = get_settings(self.request.user)
        #     if settings.current_profile.pk == object.pk:
        #         profile = get_profiles(settings.user).exclude(pk=object.pk).first()
        #         settings.current_profile = profile
        #         settings.save()
        # except Exception as outer_error:
        #     messages.error(
        #         self.request, "You have no profiles to set as your current profile."
        #     )

        messages.success(self.request, "Resource Deleted!")
        return super(DeleteResourceView, self).delete(*args, **kwargs)


def resources_view(request):
    context = get_default_context(request.user)
    context['resources'] = get_resources()
    context['types'] = [type[1] for type in TYPE_CHOICES]
    return render(request, 'marketing/resources.html', context)
