
from rest_framework import serializers
from core.model.Student import Student
from core.serializers.ScheduleSerializer import ScheduleSerializer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        depth=1
