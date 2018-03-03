from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from . import functions


class SlackAuthentication(BaseAuthentication):

    def authenticate(self, request):
        msg_data = request.data
        if msg_data.get('token') != settings.SLACK_VERIFICATION_TOKEN:
            raise exceptions.AuthenticationFailed('Incorrect auth token.')   
        if msg_data.get('type') == 'url_verification':
            challenge = msg_data.get('challenge')       
            return Response(data=challenge, status=status.HTTP_200_OK)


class Event(APIView):

    authentication_classes = [SlackAuthentication]

    def post(self, request, *args, **kwargs):
        event = request.data.get('event')
        if event and not event.get('subtype') == 'bot_message':
            event_type = event['type']
            func = getattr(functions, event_type, None)
            if func:
                func(request.data)
        return Response(status=status.HTTP_200_OK)

event_view = Event.as_view()


class Command(APIView):

    authentication_classes = [SlackAuthentication]

    def post(self, request, *args, **kwargs):
        command = request.data['command'].replace('/', '')
        func = getattr(functions, command, None)
        if not func:
            data = {
                "response_type": "ephemeral",
                "text": "That command doesn't exist."
            }
            return Response(data, status=status.HTTP_200_OK)
        res = func(request.data)
        return Response(res, status=status.HTTP_200_OK)

command_view = Command.as_view()
