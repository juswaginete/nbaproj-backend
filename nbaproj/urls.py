"""nbaproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from teams.views import TeamsView, CustomTeamView, DeleteTeamView
from players.views import PlayersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('teams/', TeamsView.as_view(), name='nba_teams'),
    path('my-teams/', CustomTeamView.as_view(), name='nba_my_teams'),
    path('delete-team/<int:pk>', DeleteTeamView.as_view(), name='delete_nba_my_team'),
    path('players/', PlayersView.as_view(), name='nba_players')
]
