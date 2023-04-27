from django.urls import path

from .views import ScreenShotsListView


urlpatterns = [
    path("", ScreenShotsListView.as_view(), name="home"),
]
