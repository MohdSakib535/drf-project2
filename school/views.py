from django.shortcuts import render
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .models import Student,Studentclean
from .serializer import serializer_data ,serializer_data2
from rest_framework import status
from rest_framework import generics
# Create your views here.

class lc_data(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=serializer_data

    def get(self,*args,**kwargs):

        print('args--',args)
        print('kwargs--',kwargs)
        return self.list(*args,**kwargs)

    def post(self,*args,**kwargs):
        print('args- p-', args)
        print('kwargs--', kwargs)
        return self.create(*args,**kwargs)

class rud_data(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=serializer_data

    def get(self,*args,**kwargs):
        return self.retrieve(*args,**kwargs)

    def put(self,*args,**kwargs):
        return self.update(*args,**kwargs)
    
    def delete(self,*args,**kwargs):
        return self.destroy(*args,**kwargs)




class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = serializer_data

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        print('----',response)

        if response.status_code == status.HTTP_201_CREATED:
            student_data = response.data
            student_clean_instance = Studentclean.objects.create(
                name=student_data['name'],
                roll=student_data['roll'],
                city=student_data['city']
            )

            # You can customize the response if needed
            response.data['student_clean_id'] = student_clean_instance.id

        return response

