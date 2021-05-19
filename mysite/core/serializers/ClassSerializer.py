from rest_framework import serializers
from core.model.Class import Class

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'