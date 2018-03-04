from django.test import TestCase

from .models import SlackModel


class TestModel(SlackModel):
    """Model for testing"""


COMMAND_REQUEST = {
    "token": "gIkuvaNzQIHg97ATvDxqgjtO",
    "team_id": "T0001",
    "team_domain": "example",
    "enterprise_id": "E0001",
    "enterprise_name": "Globular%20Construct%20Inc",
    "channel_id": "C2147483705",
    "channel_name": "test",
    "user_id": "U2147483697",
    "user_name": "Steve",
    "command": "/weather",
    "text": "94070",
    "response_url": "https://hooks.slack.com/commands/1234/5678",
    "trigger_id": "13345224609.738474920.8088930838d88f008e0"
}


EVENT_REQUEST = {
    "token": "z26uFbvR1xHJEdHE1OQiO6t8",
    "team_id": "T061EG9RZ",
    "api_app_id": "A0FFV41KK",
    "event": {
            "type": "reaction_added",
            "user": "U061F1EUR",
            "item": {
                    "type": "message",
                    "channel": "C061EG9SL",
                    "ts": "1464196127.000002"
            },
            "reaction": "slightly_smiling_face"
    },
    "event_ts": "1465244570.336841",
    "type": "event_callback",
    "authed_users": [
            "U061F7AUR"
    ]
}


class SlackTestCase(TestCase):

    def test_slack_command(self):
        TestModel.objects.create(data=COMMAND_REQUEST, type=TestModel.COMMAND)
        weather_his = TestModel.objects.filter(data__command='/weather')
        self.assertEqual(COMMAND_REQUEST, weather_his.first().data)

    def test_slack_event(self):
        TestModel.objects.create(data=EVENT_REQUEST, type=TestModel.EVENT)
        reaction_added_his = TestModel.objects.filter(data__event__type='reaction_added')
        self.assertEqual(EVENT_REQUEST, reaction_added_his.first().data)
