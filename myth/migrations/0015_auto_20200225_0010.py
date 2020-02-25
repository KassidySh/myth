# Generated by Django 3.0.3 on 2020-02-25 00:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myth', '0014_region_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='being',
            name='favorite_god',
            field=models.ManyToManyField(blank=True, related_name='favorite_god', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='story',
            name='favorite_story',
            field=models.ManyToManyField(blank=True, related_name='favorite_story', to=settings.AUTH_USER_MODEL),
        ),
    ]
