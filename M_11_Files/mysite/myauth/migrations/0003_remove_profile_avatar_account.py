# Generated by Django 4.2 on 2023-04-16 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myauth.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myauth', '0002_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('agreement_accept', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=myauth.models.account_avatar_directory_path)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]