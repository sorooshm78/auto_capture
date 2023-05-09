import os

from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete


def get_file_upload_path(instance, filename):
    return f"shots/{instance.user.username}/{filename}"


class ScreenShot(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="screenshots"
    )
    image = models.ImageField(upload_to=get_file_upload_path)
    created = models.DateTimeField()

    def __str__(self):
        return f"{self.user} {self.created}"


@receiver(post_delete, sender=ScreenShot)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `ScreenShot` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


class OnlineClient(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
