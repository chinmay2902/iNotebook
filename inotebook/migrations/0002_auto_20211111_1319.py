# Generated by Django 3.2.9 on 2021-11-11 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inotebook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='creater',
        ),
        migrations.AddField(
            model_name='notes',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
