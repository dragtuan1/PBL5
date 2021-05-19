from rest_framework import serializers
from core.model.Account import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        depth=1

        def create(self, validated_data):
            return Account.objects.create(validated_data)