from django.db.models import fields
from rest_framework import serializers
from .models import User, Profile

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'artist_name', 'password')
        extra_kwargs = {'password': {
            'write_only': True
            }}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    model = Profile
    fields = (
        'first_name', 'last_name',
        'country', 'gender',
        'record_label', 'image', 
    )