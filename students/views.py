from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Student
from .serializers import StudentSerializer
# Create your views here.


class AllStudents(APIView)
    def get(self, request):
        modelData = Student.objects.all()
        serializer = StudentSerializer(modelData, many=True)
        return Response(serializer.data)

    def post(self, request)
        serializer = StudentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def one_student(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_200_OK)
