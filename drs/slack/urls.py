from django.urls import path

from .views import event_view, command_view


urlpatterns = [
    path('events/', event_view),
    path('commands/', command_view),
]
