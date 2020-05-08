from .models import (Project, Task, CurrentProject, Location, Platform,
                     SamplePost, LivePost, Resource)


def get_projects(user):
    return Project.objects.filter(people__username=user.username)


def set_current_project(user, new_current_project_pk):
    curr = CurrentProject.objects.get(user=user)
    curr.project = Project.objects.get(pk=new_current_project_pk)
    curr.save()


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


def get_resources():
    return {
        "images": Resource.objects.filter(type="I"),
        "documents": Resource.objects.filter(type="D"),
        "misc": Resource.objects.filter(type="M")
    }


def get_default_context(user):
    context = {
        "projects": get_projects(user),
        "current_project": get_current_project(user),
        "platforms": get_platforms()
    }
    return context


def get_class_based_default_context(context, user):
    default_context = get_default_context(user)
    for item in get_default_context(user):
        context[item] = default_context[item]
    return context
