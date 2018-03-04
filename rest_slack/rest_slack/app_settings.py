import os

from django.conf import settings


SLACK_CLIENT_ID = getattr(settings, 'SLACK_CLIENT_ID', os.environ.get('SLACK_CLIENT_ID'))


SLACK_CLIENT_SECRET =  getattr(settings, 'SLACK_CLIENT_SECRET', os.environ.get('SLACK_CLIENT_SECRET'))


SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', os.environ.get('SLACK_VERIFICATION_TOKEN'))


SLACK_BOT_USER_TOKEN = getattr(settings, 'SLACK_BOT_USER_TOKEN', os.environ.get('SLACK_BOT_USER_TOKEN'))


REST_FRAMEWORK = getattr(settings, 'REST_FRAMEWORK', {'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'})
