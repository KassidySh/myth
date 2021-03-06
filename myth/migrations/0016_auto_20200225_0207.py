# Generated by Django 3.0.3 on 2020-02-25 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myth', '0015_auto_20200225_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favegod',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favestory',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='loggedon', to=settings.AUTH_USER_MODEL),
        ),
    ]
