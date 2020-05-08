from .models import (Project, Task, CurrentProject, Location, Platform,
                     SamplePost, LivePost)


def get_projects(user):
    return Project.objects.filter(people__username=user.username)


def get_current_project(user):
    return CurrentProject.objects.get(user=user).project


def get_sample_posts(user):
    return SamplePost.objects.filter(project=get_current_project(user))


def get_live_posts(user):
    return LivePost.objects.filter(sample_post__project=get_current_project(user))


def get_platforms():
    return Platform.objects.all()


def get_tasks(user, status):
    return {
        "to_user": Task.objects.filter(assigned_to=user, completed=status).order_by('due_date'),
        "by_user": Task.objects.filter(creator=user, completed=status).order_by('due_date')
    }


def get_locations(user):
    return Location.objects.filter(project=get_current_project(user))


def get_resources(user):
    resources = []
    for post in get_sample_posts(user):
        resources = resources + list(post.resources.all())
    return resources


def get_default_context(user):
    context = {
        "projects": get_projects(user),
        "current_project": get_current_project(user),
        "platforms": get_platforms()
    }
    return context
