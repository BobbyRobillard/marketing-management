from django.db import models

from django.contrib.auth.models import User

name_length = 50
abbreviated_name_length = 10
description_length = 150
url_length = 300

TYPE_CHOICES = (
    ('I', 'Image'),
    ('D', 'Document'),
    ('M', 'Misc'),
)


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=name_length)
    abbreviated_name = models.CharField(max_length=abbreviated_name_length)
    people = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class CurrentProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Platform(models.Model):
    name = models.CharField(max_length=name_length)
    abbreviated_name = models.CharField(max_length=abbreviated_name_length)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=name_length)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    url = models.CharField(max_length=url_length)
    description = models.CharField(max_length=description_length)
    posts_per_week = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    tone = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_sales(self):
        posts = LivePost.objects.filter(location=self)
        sales = 0
        for post in posts:
            sales += post.get_sales()
        return sales


class Resource(models.Model):
    name = models.CharField(max_length=name_length)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    url = models.CharField(max_length=url_length)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_posts_used_in(self):
        return SamplePost.objects.filter(resources__pk=self.pk)


class SamplePost(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    caption = models.CharField(max_length=500)
    title = models.CharField(max_length=description_length)
    tags = models.CharField(max_length=description_length)
    resources = models.ManyToManyField(Resource)

    def __str__(self):
        return self.title


class LivePost(models.Model):
    is_active = models.BooleanField(default=True)
    poster = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, null=True, blank=True)
    sample_post = models.ForeignKey(SamplePost, on_delete=models.CASCADE)
    number_of_likes = models.PositiveIntegerField()
    number_of_shares = models.PositiveIntegerField()
    number_of_comments = models.PositiveIntegerField()
    post_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.sample_post.title

    def get_sales(self):
        return 50

    def get_number_of_interactions(self):
        return (self.number_of_likes + self.number_of_shares + self.number_of_comments)


class Task(models.Model):
    create_post = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_to')
    locations = models.ManyToManyField(Location)
    sample_post = models.ForeignKey(SamplePost, null=True, blank=True, on_delete=models.CASCADE)
    live_post = models.ForeignKey(LivePost, null=True, blank=True, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        if self.create_post:
            str = "Publish Post | {0}".format(self.sample_post)
        else:
            str = "Monitor Post | {0}".format(self.live_post)

        return str


class Webstore(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    private_api_key = models.CharField(max_length=150)
    public_api_key = models.CharField(max_length=150)
