from django.db import models

from posting.models import Post

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    recieved = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def get_amount_owed(self):
        return self.get_amount_earned() * self.recieved / 100

    def get_amount_earned(self):
        return 2000

    def get_posts(self):
        return Post.objects.filter(project=self).order_by('name')

class StoreAuthentication(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
