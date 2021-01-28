from rest_framework import serializers

from ..profiles.models import Profile, ProfileStatus


class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ("user", "desc", "colour")


class ProfileColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "colour"


class ProfileStatusSerializer(serializers.ModelSerializer):

    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileStatus
        fields = ("user_profile", "status_content", "created_at", "updated_at")
