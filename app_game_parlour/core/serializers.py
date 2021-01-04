from rest_framework import serializers
from core.models import Player


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
