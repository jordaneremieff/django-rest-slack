from django.contrib import admin

from .models import SlackModel


class SlackAdmin(admin.ModelAdmin):
    """Simple admin view for looking over data"""

admin.site.register(SlackModel, SlackAdmin)
