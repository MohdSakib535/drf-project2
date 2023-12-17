from django.shortcuts import render
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .models import Student,Studentclean
from .serializer import serializer_data ,serializer_data2
from rest_framework import status
from rest_framework import generics
from .checker import clean_city_data
# Create your views here. go

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

    def perform_create(self, serializer):
        instance = serializer.save()
        print('ins---',instance.name)
        city_D=clean_city_data(instance.city)
        print('----',city_D)
        inst_data={'name':city_D,
                   'roll':instance.roll,
                   'city':instance.name,
                   }
        clean1_serializer = serializer_data2(data=inst_data)
        print('clean1_serializer----',clean1_serializer)
        if clean1_serializer.is_valid():
            clean1_serializer.save()
        else:
            print('not valid')


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


        if response.status_code == status.HTTP_201_CREATED:
            student_data = response.data
            student_clean_instance = Studentclean.objects.create(
                name=student_data['name'],
                roll=student_data['roll'],
                city=student_data['city']
            )



        return response

