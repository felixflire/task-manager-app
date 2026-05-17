from django.urls import path

from . import views

app_name = "tasksapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name = "add"),
    path("delete/", views.delete, name = "delete"),
    path("toggle/<int:task_id>/", views.toggle_complete, name="toggle_complete")
]
