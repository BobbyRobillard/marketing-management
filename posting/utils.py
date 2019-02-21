from .models import Post, ApplicableCode

from administration.models import Project, StoreAuthentication

def get_coupon_code_choices(post_pk):
    api = StoreAuthentication.objects.get(project=Post.objects.get(pk=post_pk).project).connect()
    return api.get("coupons").json()

def create_post(data, project_pk):
    p = Post.objects.create(name=data['name'], project=Project.objects.get(pk=project_pk),
                        url=data['url'], posted=data['posted'], topic=data['topic'])

def get_unused_codes(post_pk):
    codes = []
    used_codes = get_used_codes(post_pk)
    for code in get_coupon_code_choices(post_pk):
        if code not in used_codes:
            codes.append(code)
    return codes

def get_used_codes(post_pk):
    return ApplicableCode.objects.filter(post=Post.objects.get(pk=post_pk))
