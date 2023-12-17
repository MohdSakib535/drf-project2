from .models import Student,Studentclean
from rest_framework import serializers

class serializer_data(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class serializer_data2(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'