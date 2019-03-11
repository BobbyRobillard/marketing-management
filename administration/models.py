from django.db import models

from posting.models import Post, Topic

from woocommerce import API

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    percent_received = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    add_coupon_url = models.URLField()

    def __str__(self):
        return self.name

    def get_amount_owed(self):
        return self.get_amount_earned() * float(self.percent_received) / 100

    def get_amount_earned(self):
        amount = 0
        for p in self.get_posts():
            amount += p.get_amount_earned()
        return amount

    def get_posts(self):
        return Post.objects.filter(project=self).order_by('name')

    def connect(self):
        return StoreAuthentication.objects.get(project=self).connect()

    def get_topics(self):
        return Topic.objects.filter(project=self)

class StoreAuthentication(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    url = models.URLField()
    consumer_key = models.CharField(max_length=100)
    consumer_secret = models.CharField(max_length=100)
    wp_api = models.BooleanField(default=True)
    version = models.CharField(max_length=10)

    def __str__(self):
        return str(self.project) + " Auth"

    def connect(self):
        return API(
            url=self.url,
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            wp_api=self.wp_api,
            version=self.version
        )
