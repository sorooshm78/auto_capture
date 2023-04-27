from django import forms

from .models import ScreenShot


class ScreenShotForm(forms.ModelForm):
    class Meta:
        model = ScreenShot
        fields = (
            "image",
            "created",
        )
