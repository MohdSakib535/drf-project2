from django.shortcuts import render
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .models import Student,Studentclean
from .serializer import serializer_data ,serializer_data2
from rest_framework import status
from rest_framework import generics
from .checker import clean_city_data
from django.http import HttpResponse
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




related_functions={'city':clean_city_data}

not_map_field={'id'}
raw_models = {"student": Student, "Studentclean": Studentclean}

def raw_to_clean(request):
    d1={}
    dta=Student.objects.all()
    for k in raw_models:
        d1[k] = list(set([f.name for f in raw_models[k]._meta.fields]) - not_map_field)
    print(d1)

    # for i,j in zip(Student._meta.fields,dta):
    #     print('k----',i.name)
    #     print('j----',j)


    return HttpResponse('ok')


from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime
# @api_view(['GET', 'POST'])
# def insert_raw_data(request):
#     try:
#         d={'name':'sakib','roll':'22','city':'Delhi','dtt_data':'25-12-2023 00:00:00'}
#         s1=Student.objects.filter(**d).exclude(dtt_data=d['dtt_data'])
#         print('s1-------',type(s1))
#         if not s1.exists():
#             formatted_date = datetime.datetime.strptime(d['dtt_data'],'%d-%m-%Y').strftime('%Y-%m-%d')
#             print('f----',formatted_date)
#             d['dtt_data']=formatted_date
#             s=serializer_data(data=d)
#             s.is_valid(raise_exception=True)
#             s.save()
#             print('success---------')
#             return Response(s.data)
#         return Response({'detail': 'matching record found.'})
#     except Exception as e:
#         print(e)





@api_view(['GET', 'POST'])
def insert_raw_data(request):
    try:
        dtaw='10/22/20 '
        d = {'name': 'k', 'roll': '22', 'city': 'Delhi', 'datetime_data':dtaw}
        h2=datetime.datetime.strptime(d['datetime_data'],'%m/%d/%Y %I:%M %p')
        print('h2---',h2)


        formatted_datetime = datetime.datetime.strptime(d['datetime_data'], '%m/%d/%Y %I:%M %p').strftime('%Y-%m-%d %H:%M:%S ')
        print('f----', formatted_datetime)
        d['datetime_data'] = formatted_datetime
        print('d-----',d)

        s1 = Student.objects.filter(**d)
        print('s1-------', type(s1))
        if not s1.exists():
            # formatted_datetime = datetime.datetime.strptime(d['datetime_data'], '%d-%m-%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
            # print('f----', formatted_datetime)
            # d['datetime_data'] = formatted_datetime
            s = serializer_data(data=d)  # Replace with the actual serializer class
            print('-------',d['datetime_data'])
            s.is_valid(raise_exception=True)
            s.save()
            print('success---------')
            return Response(s.data, status=status.HTTP_201_CREATED)
        else:
            # Add a default response for cases where the condition is not met
            return Response({'detail': ' matching record found.'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        print(e)
        # Handle exceptions and return an error response if needed
        return Response({'detail': 'An error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
