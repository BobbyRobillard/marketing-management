# Generated by Django 2.0 on 2019-02-27 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0002_auto_20190225_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postlocation',
            name='earned',
        ),
    ]
