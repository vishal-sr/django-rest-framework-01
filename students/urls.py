from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllStudents.as_view()),
    path("<int:id>", views.OneStudent.as_view())
]
