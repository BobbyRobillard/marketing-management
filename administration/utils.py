from .models import Project

def get_all_projects():
    return Project.objects.all()
