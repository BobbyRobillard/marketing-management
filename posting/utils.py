from .models import Post, ApplicableCode

from administration.models import Project

def get_coupon_code_choices():
    return [('test123', 'test123') for i in range(0, 3)]

def create_post(data, project_pk):
    p = Post.objects.create(name=data['name'], project=Project.objects.get(pk=project_pk),
                        url=data['url'], posted=data['posted'], topic=data['topic'],
                            earned=data['earned'])
    for code in data['codes']:
        ApplicableCode.objects.create(code=code, post=p)
