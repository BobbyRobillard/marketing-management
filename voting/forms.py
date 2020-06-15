from django import forms

from .models import Poll


class AddPollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'url']
