from .models import Post, ApplicableCode

from administration.models import Project

def get_coupon_code_choices():
    return ['abc', '123', 'cats']

def create_post(data, project_pk):
    p = Post.objects.create(name=data['name'], project=Project.objects.get(pk=project_pk),
                        url=data['url'], posted=data['posted'], topic=data['topic'],
                            earned=data['earned'])
    for code in data['codes']:
        ApplicableCode.objects.create(code=code, post=p)

def get_unused_codes(post_pk):
    codes = []
    used_codes = get_used_codes(post_pk)
    for code in get_coupon_code_choices():
        if code not in used_codes:
            codes.append(code)
    return codes

def get_used_codes(post_pk):
    return [code.code for code in ApplicableCode.objects.filter(post=Post.objects.get(pk=post_pk))]