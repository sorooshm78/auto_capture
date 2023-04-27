from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ScreenShot


class ScreenShotsListView(LoginRequiredMixin, ListView):
    model = ScreenShot
    template_name = "web/home.html"
    context_object_name = "shots"

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(user=self.request.user)
        return query
