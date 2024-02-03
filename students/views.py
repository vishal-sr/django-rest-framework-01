from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import mixins, generics

from .models import Student
from .serializers import StudentSerializer
# Create your views here.


class AllStudents(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class OneStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
