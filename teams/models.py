from django.db import models


class Teams(models.Model):
    teamName = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    abbreviation = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.teamName 

    class Meta:
        verbose_name_plural = "Teams"