# Generated by Django 2.0 on 2019-02-11 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='recieved',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
