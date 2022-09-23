from django import forms

from teams.models import Teams


class TeamsForm(forms.ModelForm):

    class Meta:
        model = Teams
        fields = '__all__'