from datetime import datetime, timezone
from django.utils.timesince import timesince
from rest_framework import serializers

from core.models import Player, Game


class GameSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Game
        exclude = ("updated_at",)

    def get_time_since_publication(self, obj):
        created_at = obj.created_at
        now = datetime.now(timezone.utc)
        time_delta = timesince(created_at, now=now)
        return time_delta


class PlayerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    player_id = serializers.UUIDField(required=False)
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.player_id = validated_data.get("player_id", instance.player_id)
        instance.save()
        return instance
