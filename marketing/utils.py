from .models import Project


def get_projects(user):
    return Project.objects.filter(people__username=user.username)
