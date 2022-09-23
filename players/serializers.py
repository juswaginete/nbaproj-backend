from rest_framework import serializers

from players.models import Players


class PlayersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Players
        fields = '__all__'