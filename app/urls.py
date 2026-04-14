from django.urls import path
from .views import index, answer

urlpatterns = [
    path("", index, name="index"),
    path("answer/", answer, name="answer"),
]
