# Generated by Django 2.0 on 2019-02-15 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0003_auto_20190212_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
