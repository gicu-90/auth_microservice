from rest_framework import serializers
from account.models import UserData

class AuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "email", "password"]

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'])
        
        user.set_password(validated_data['password'])
        user.save()
        return user
