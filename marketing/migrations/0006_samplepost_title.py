# Generated by Django 3.0 on 2020-05-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0005_location_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='samplepost',
            name='title',
            field=models.CharField(default='Demo Post', max_length=150),
            preserve_default=False,
        ),
    ]