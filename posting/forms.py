from django import forms

from .utils import get_coupon_code_choices

from .models import Topic

class PostForm(forms.Form):
    name = forms.CharField(max_length=100)
    topic = forms.ModelChoiceField(queryset=Topic.objects.all())
    url = forms.URLField()
    posted = forms.DateField()
    earned = forms.DecimalField(max_digits=10, decimal_places=2, initial=0)
    codes = forms.MultipleChoiceField(choices=get_coupon_code_choices())
