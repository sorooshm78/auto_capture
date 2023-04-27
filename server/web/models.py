from django.db import models
from django.conf import settings


def get_file_upload_path(instance, filename):
    return f"shots/{instance.user.username}/{filename}"


class ScreenShot(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="screenshots"
    )
    image = models.ImageField(upload_to=get_file_upload_path)
    datetime = models.DateTimeField(auto_now_add=True)
