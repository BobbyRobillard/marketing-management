from .models import Project, Task


def get_projects(user):
    return Project.objects.filter(people__username=user.username)


def get_default_context(user):
    context = {
        "projects": get_projects(user)
    }
    return context


def get_tasks(user, status):
    return {
        "to_user": Task.objects.filter(assigned_to=user, completed=status).order_by('due_date'),
        "by_user": Task.objects.filter(creator=user, completed=status).order_by('due_date')
    }
