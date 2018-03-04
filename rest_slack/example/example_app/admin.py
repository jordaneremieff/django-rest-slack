from django.contrib import admin

from .models import ExampleSlackModel


class ExampleSlackAdmin(admin.ModelAdmin):
    """Simple admin view for looking over data"""

admin.site.register(ExampleSlackModel, ExampleSlackAdmin)
