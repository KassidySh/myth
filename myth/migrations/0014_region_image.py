# Generated by Django 3.0.3 on 2020-02-22 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myth', '0013_auto_20200219_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='image',
            field=models.TextField(blank=True),
        ),
    ]