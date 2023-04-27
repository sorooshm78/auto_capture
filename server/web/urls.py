from django.urls import path

from . import views


urlpatterns = [
    path("", views.ScreenShotsListView.as_view(), name="home"),
    path("upload/", views.ScreenShotsCreateView.as_view(), name="create_shot"),
    path("delete/<pk>/", views.ScreenShotsDeleteView.as_view(), name="delete_shot"),
]
