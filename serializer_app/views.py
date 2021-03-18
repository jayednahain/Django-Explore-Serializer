from django.shortcuts import render
from serializer_app.models import Student
from serializer_app.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET','POST'])
def studetn_list(request):


   #to know the student details

   if request.method == 'GET':

      students = Student.objects.all()
      serializer = StudentSerializer(students,many=True)
      return Response(serializer.data)

   #for creating a student

   elif request.method == 'POST':
      serializer= StudentSerializer(data=request.data) # get the data and serialize it
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#primary key based operation
#updateing student and deleting student from database !
#by using the primary key


@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
   try:
      student = Student.objects.get(pk=pk) # getting singel student !
   except Student.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

   #handle the request !

   if request.method =='GET':
      serializer = StudentSerializer(student) #we have already take the student as a object at friest ! now pass it through the serializer !
      return  Response(serializer.data)

   elif request.method =='PUT': #put for update operation !

      serializer= StudentSerializer(student,data=request.data) #take the data we want to change ! and overwrite it
      if serializer.is_valid(): #if the data we want to change is valled !
         serializer.save() # and save it
         return Response(serializer.data)

      return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



   elif request.method =='DELETE':
      student.delete()
      return  Response(status=status.HTTP_204_NO_CONTENT)

