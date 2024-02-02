from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics

from .models import Student
from .serializers import StudentSerializer
# Create your views here.


class AllStudents(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class OneStudent(APIView):
    def get_student(id):
        try:
            student = Student.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return student

    def get(self, request, id):
        student = OneStudent.get_student(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        student = OneStudent.get_student(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = OneStudent.get_student(id=id)
        student.delete()
        return Response(status=status.HTTP_200_OK)
