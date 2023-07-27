from django.contrib import admin
from .models import MusicGroups


@admin.register(MusicGroups)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ("group_name", "founder", "date_created")
    prepopulated_fields = {"slug": ("group_name",)}
