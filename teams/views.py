import json
import http.client

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from nba_api.stats.endpoints import teamyearbyyearstats
from nba_api.stats.static import teams

from teams.serializers import TeamsSerializer
from teams.models import Teams


class TeamsView(APIView):
    def get(self, request, *args, **kwargs):
        if request.GET.get('team_id'):
            response_data = teamyearbyyearstats.TeamYearByYearStats(team_id=request.GET.get('team_id')).get_dict()
        else:
            response_data = teams.get_teams()

        return Response(response_data)

    def post(self, request, format=None):
        serializer = TeamsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTeamView(APIView):
    def get(self, request, format=None):
        teams = [{ 'teamId': team.id, 'teamName': team.teamName } for team in Teams.objects.all()]
        return Response(teams)


class DeleteTeamView(APIView):
    def get_object(self, pk):
        try:
            return Teams.objects.get(pk=pk)
        except Teams.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
