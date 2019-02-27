from django import forms

from .utils import get_coupon_code_choices

from .models import Post, PostLocation

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if self.has_changed():
            if Post.objects.filter(name=name).exists():
                raise forms.ValidationError("Error, a Post with this name already exists.")
        return name

class PostLocationForm(forms.ModelForm):
    class Meta:
        model = PostLocation
        exclude = ('earned',)
