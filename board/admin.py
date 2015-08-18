from django.contrib import admin
from .models import Challenge, Participant


class Participant(admin.TabularInline):
    model = Participant


class ChallengeAdmin(admin.ModelAdmin):
    inlines = (Participant, )


admin.site.register(Challenge, ChallengeAdmin)
