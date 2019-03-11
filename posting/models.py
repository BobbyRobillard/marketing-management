from django.db import models

name_length = 100

class Topic(models.Model):
    name = models.CharField(max_length=name_length, unique=True)
    project = models.ForeignKey('administration.Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_posts(self):
        return Post.objects.filter(topic=self)

    def get_num_posts(self):
        return len(self.get_posts())

class Post(models.Model):
    name = models.CharField(max_length=name_length)
    project = models.ForeignKey('administration.Project', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_amount_earned(self):
        amount = 0
        for l in PostLocation.objects.filter(post=self):
            amount = amount + l.get_amount_earned()
        return amount

    def get_amount_owed(self):
        return self.get_amount_earned()/100 * float(self.project.percent_received)

class Platform(models.Model):
    type = models.CharField(max_length=name_length, unique=True)

    def __str__(self):
        return self.type

class PostLocation(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, blank=True, null=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=name_length, unique=True)
    url = models.URLField(unique=True)
    posted_on = models.DateField()

    def get_amount_earned(self):
        earned = 0
        api = self.post.project.connect()
        for order in api.get("orders?per_page=100").json():
            if self.code in [coupon['code'] for coupon in order['coupon_lines']]:
                amount = 0
                for item in order['line_items']:
                    amount = amount + float(item['subtotal'])
                earned = earned + amount
        return earned
