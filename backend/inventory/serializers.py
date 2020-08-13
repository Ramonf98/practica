from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Person
class UserSerializer(serializers.Serializer):
    """
    Serializer for model User
    """
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        create a user an validate the data
        """
        instance = User()
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_user(self, data:str):
        users = User.objects.filter(username= data)
        if len(users) != 0:
            raise serializers.ValidationError("Este nombre de usuario ya existe")
        return data

    def update(self, instance, validated_data):
        return 0


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'