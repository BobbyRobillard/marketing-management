from django.db import models

name_length = 100

class Topic(models.Model):
    name = models.CharField(max_length=name_length, unique=True)
    project = models.ForeignKey('administration.Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=name_length)
    project = models.ForeignKey('administration.Project', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    url = models.URLField()
    posted = models.DateField()
    earned = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def get_amount_earned(self):
        api = self.project.connect()
        earned = 0
        for order in api.get("orders?per_page=100").json():
            if ApplicableCode.objects.filter(code__in=[coupon['code'] for coupon in order['coupon_lines']], post=self).exists():
                amount = 0
                for item in order['line_items']:
                    amount = amount + float(item['subtotal'])
                earned = earned + amount
        return earned

    def get_amount_owed(self):
        return self.get_amount_earned()/100 * float(self.project.percent_received)

class ApplicableCode(models.Model):
    code = models.CharField(max_length=name_length)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post) + self.code
