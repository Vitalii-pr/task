from rest_framework import serializers

from api.accounts import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}

    def create(self, validated_data):
        """create and return new user"""
        new_user = models.UserProfile.objects.create_user(**validated_data)
        return new_user
