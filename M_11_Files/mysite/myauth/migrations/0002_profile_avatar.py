# Generated by Django 4.2 on 2023-04-15 07:38

from django.db import migrations, models
import myauth.models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=myauth.models.account_avatar_directory_path),
        ),
    ]
