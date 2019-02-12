from django.db import models

name_length = 100

class Topic(models.Model):
    name = models.CharField(max_length=name_length, unique=True)
    project = models.ForeignKey('administration.Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=name_length, unique=True)
    project = models.ForeignKey('administration.Project', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    url = models.URLField()
    posted = models.DateField()
    earned = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def get_amount_earned(self):
        return 1000

    def get_amount_owed(self):
        return self.get_amount_earned()/100 * float(self.project.recieved)

class ApplicableCode(models.Model):
    code = models.CharField(max_length=name_length)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post) + self.code
