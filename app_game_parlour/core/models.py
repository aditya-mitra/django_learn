import uuid
from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    player_id = models.UUIDField(default=uuid.uuid4, unique=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
