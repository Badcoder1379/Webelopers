# Generated by Django 2.2.7 on 2019-11-08 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='author',
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_photo',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]