from django.db import models

name_length = 100

class Topic(models.Model):
    name = models.CharField(max_length=name_length)
    project = models.ForeignKey('administration.Project', on_delete=models.CASCADE)

class Post(models.Model):
    name = models.CharField(max_length=name_length)
    project = models.ForeignKey('administration.Project', on_delete=models.CASCADE)
    url = models.URLField()
    posted = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    earned = models.DecimalField(max_digits=10, decimal_places=2, default=0)
