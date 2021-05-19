from rest_framework import serializers
from core.model.Info import Info

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'
        