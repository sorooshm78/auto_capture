from django.urls import path

from . import views


urlpatterns = [
    path("", views.RunCommandView.as_view(), name="command"),
]
