from django.contrib import admin
from .models import Seasons


@admin.register(Seasons)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "start_date")
    prepopulated_fields = {"slug": ("title",)}
