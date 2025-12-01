from rest_framework import serializers

from .models import UserProfile


class UserProfileSerialzier(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = UserProfile
        fields = ["username", "avatar", "bio"]
