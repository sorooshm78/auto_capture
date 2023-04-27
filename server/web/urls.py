from django.urls import path

from .views import ScreenShotsListView, ScreenShotsCreateView


urlpatterns = [
    path("", ScreenShotsListView.as_view(), name="home"),
    path("upload/", ScreenShotsCreateView.as_view(), name="create_shot"),
]
