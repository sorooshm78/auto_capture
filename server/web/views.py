from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import ScreenShot
from .forms import ScreenShotForm


class ScreenShotsListView(LoginRequiredMixin, ListView):
    model = ScreenShot
    template_name = "web/home.html"
    context_object_name = "shots"

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(user=self.request.user).order_by("-created")
        return query


class ScreenShotsCreateView(LoginRequiredMixin, CreateView):
    form_class = ScreenShotForm
    template_name = "web/create_shot.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ScreenShotsDeleteView(LoginRequiredMixin, DeleteView):
    model = ScreenShot
    template_name = "web/confirm_delete_shot.html"
    success_url = reverse_lazy("home")
