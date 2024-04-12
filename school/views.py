from django.shortcuts import render
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .models import Student,Studentclean,clean_Agent,clean_properties,Agent,properties,Teacher
from .serializer import serializer_data ,serializer_data2
from rest_framework import status
from rest_framework import generics
from .checker import clean_city_data,clean_roll_data,clean_name_data
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

    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     print('ins---',instance.name)
    #     city_D=clean_city_data(instance.city)
    #     print('----',city_D)
    #     inst_data={'name':city_D,
    #                'roll':instance.roll,
    #                'city':instance.name,
    #                }
    #     clean1_serializer = serializer_data2(data=inst_data)
    #     print('clean1_serializer----',clean1_serializer)
    #     if clean1_serializer.is_valid():
    #         clean1_serializer.save()
    #     else:
    #         print('not valid')


class rud_data(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=serializer_data

    def get(self,*args,**kwargs):
        return self.retrieve(*args,**kwargs)

    def put(self,*args,**kwargs):
        return self.update(*args,**kwargs)

    def delete(self,*args,**kwargs):
        return self.destroy(*args,**kwargs)




# class StudentCreateView(generics.CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = serializer_data
#
#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#
#
#         if response.status_code == status.HTTP_201_CREATED:
#             student_data = response.data
#             student_clean_instance = Studentclean.objects.create(
#                 name=student_data['name'],
#                 roll=student_data['roll'],
#                 city=student_data['city']
#             )
#         return response





#
# related_functions={'city':clean_city_data}
#
# not_map_field={'id'}
# raw_models = {"student": Student, "Studentclean": Studentclean}

# def raw_to_clean(request):
#     d1={}
#     dta=Student.objects.all()
#     for k in raw_models:
#         d1[k] = list(set([f.name for f in raw_models[k]._meta.fields]) - not_map_field)
#     print(d1)
#
#     # for i,j in zip(Student._meta.fields,dta):
#     #     print('k----',i.name)
#     #     print('j----',j)
#
#
#     return HttpResponse('ok')


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





# @api_view(['GET', 'POST'])
# def insert_raw_data(request):
#     try:
#         dtaw='10/22/20 '
#         d = {'name': 'k', 'roll': '22', 'city': 'Delhi', 'datetime_data':dtaw}
#         h2=datetime.datetime.strptime(d['datetime_data'],'%m/%d/%Y %I:%M %p')
#         print('h2---',h2)
#
#
#         formatted_datetime = datetime.datetime.strptime(d['datetime_data'], '%m/%d/%Y %I:%M %p').strftime('%Y-%m-%d %H:%M:%S ')
#         print('f----', formatted_datetime)
#         d['datetime_data'] = formatted_datetime
#         print('d-----',d)
#
#         s1 = Student.objects.filter(**d)
#         print('s1-------', type(s1))
#         if not s1.exists():
#             # formatted_datetime = datetime.datetime.strptime(d['datetime_data'], '%d-%m-%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
#             # print('f----', formatted_datetime)
#             # d['datetime_data'] = formatted_datetime
#             s = serializer_data(data=d)  # Replace with the actual serializer class
#             print('-------',d['datetime_data'])
#             s.is_valid(raise_exception=True)
#             s.save()
#             print('success---------')
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         else:
#             # Add a default response for cases where the condition is not met
#             return Response({'detail': ' matching record found.'}, status=status.HTTP_404_NOT_FOUND)
#
#     except Exception as e:
#         print(e)
#         # Handle exceptions and return an error response if needed
#         return Response({'detail': 'An error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#end here master



from django.utils.crypto import get_random_string
# def demo2(request):
#     d=[]
#     for i in range(10):
#         d.append(get)



# def demo3(request):
#     Student.objects.bulk_create([
#         Student(name="rani",roll="23"),
#         Student(name="ritu",roll="22"),
#         Student(name="kamlesh",roll="12"),
#         Student(name="binod",roll="26"),
#
#     ])
#
#     s1= Student.objects.order_by('-created_at')[:4]
#     print(s1)
#
#     return HttpResponse('ok')


def demo4(request):
    # d={'name':'sa45k','roll':'2345','city':'dd444elhi'}
    # d={'name':'vika2s','roll':2345,'city':'go34a'}
    d={'name':'roshan344','roll':2345}

    s1=Student.objects.filter(**d).count()
    print('s1----', s1)
    if not s1:
        serializer=serializer_data(data=d)
        serializer.is_valid(raise_exception=True)
        serializer.save()



    raw=Student.objects.all()
    s2 = Studentclean()
    for i in raw:
        s2.name=clean_name_data(i.name)
        s2.roll=clean_roll_data(i.roll)
        s2.city=clean_city_data(i.city)

        pay={'name':s2.name,'roll':s2.roll,'city':s2.city}
        s3=Studentclean.objects.filter(**pay).exists()
        if not s3:
            s2.save()
    return HttpResponse('ok')



def demo5(request):

    a1=clean_Agent.objects.only('listing_id').all()
    for i in a1:
       p1=clean_properties.objects.get(listing_id=i.listing_id)
       print(p1)
    return HttpResponse('ok')



def teacher_data(request):
    s1=Teacher(name='sameer',roll="835",city="pune")
    s1.save()
    return HttpResponse('ok')

