# Generated by Django 4.1.3 on 2022-12-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0006_delete_useravatars_profile_avatar_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_file',
            field=models.FileField(blank=True, null=True, upload_to='images/user_avatars/'),
        ),
    ]