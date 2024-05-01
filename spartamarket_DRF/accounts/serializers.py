from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer() 

    class Meta:
        model = Profile
        fields = ['user', 'nickname', 'birthday', 'gender', 'bio']

    def create(self, validated_data):
        user_data = validated_data.pop('user', {})  
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()  
            profile = Profile.objects.create(user=user, **validated_data)  
            return profile
        else:
            raise serializers.ValidationError("User data is invalid")