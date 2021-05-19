from rest_framework import serializers
from core.model.Embedd import Embedd

class EmbeddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embedd
        fields = '__all__'