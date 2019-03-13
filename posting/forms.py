from django import forms

from .utils import get_coupon_code_choices

from .models import Post, PostLocation

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostLocationForm(forms.ModelForm):
    class Meta:
        model = PostLocation
        exclude = ('earned',)
