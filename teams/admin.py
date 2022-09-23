from django.contrib import admin

from teams.models import Teams
from teams.forms import TeamsForm


class TeamsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Teams, TeamsAdmin)