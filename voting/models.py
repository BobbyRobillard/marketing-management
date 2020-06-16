from django.db import models

from django.contrib.auth.models import User

name_length = 100
url_length = 300


# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=name_length)
    url = models.CharField(max_length=url_length)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_votes(self):
        return Vote.objects.filter(poll=self)


# Create your models here.
class Vote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    is_yes = models.BooleanField()
