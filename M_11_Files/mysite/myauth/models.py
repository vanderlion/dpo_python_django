from django.contrib.auth.models import User
from django.db import models


def profile_avatar_directory_path(instance: "Profile", filename: str) -> str:
    return "account/account_{pk}/avatar/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    agreement_accept = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True, upload_to=profile_avatar_directory_path)
