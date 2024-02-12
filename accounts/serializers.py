from rest_framework import serializers
from .models import User, EventUser, Organizer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name','last_name', 'username', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        model: EventUser
        fields = '__all__'

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model:Organizer
        fields = '__all__'


class PhoneNumberSerializer(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return data

class UserProfileSerializer(serializers.ModelSerializer):
    phone = PhoneNumberSerializer()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'phone', 'user_type')