from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    recieved = models.DecimalField(max_digits=4, decimal_places=2, default=0)

class StoreAuthentication(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
