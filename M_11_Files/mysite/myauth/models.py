from django.contrib.auth.models import User
from django.db import models


def account_avatar_directory_path(instance: "Account", filename: str) -> str:
    return "account/account_{pk}/avatar/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Account(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    agreement_accept = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True, upload_to=account_avatar_directory_path)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    agreement_accept = models.BooleanField(default=False)
