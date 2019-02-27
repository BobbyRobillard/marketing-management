# Generated by Django 2.0 on 2019-02-27 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0003_remove_postlocation_earned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlocation',
            name='code',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='postlocation',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
