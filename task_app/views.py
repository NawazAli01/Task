from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Student
from .serializers import StudentSerializers
from rest_framework import generics
#
# class StudentList(APIView):
# 	permission_classes = (IsAuthenticated, )
#
# 	def get(self, request):
# 		Studentcontent = Student.objects.all()
# 		serializer = StudentSerializers(Studentcontent, many=True)
# 		return Response(serializer.data)

class ListCreateAPI(generics.ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializers
