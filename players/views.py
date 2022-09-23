import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from nba_api.stats.static import players

from players.serializers import PlayersSerializer
from players.models import Players


class PlayersView(APIView):
    def get(self, request, *args, **kwargs):
        nba_players = players.get_players()

        return Response(nba_players)