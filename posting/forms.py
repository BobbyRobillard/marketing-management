from django import forms

from .utils import get_coupon_code_choices

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('earned',)
