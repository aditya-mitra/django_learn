from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Player
from core.serializers import PlayerSerializer


@api_view(["GET", "POST"])
def player_list_view(request):
    if request.method == "GET":
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def player_detail_view(request, pk):
    try:
        player = Player.objects.get(pk=pk)
    except Player.DoesNotExist:
        return Response({"error": "player not found"})

    if request.method == "GET":
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
