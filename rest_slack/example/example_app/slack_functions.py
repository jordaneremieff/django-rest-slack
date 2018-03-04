from rest_slack.registry import Registry
from rest_slack.utils import save_slack_data

from example_app.models import ExampleSlackModel


register = Registry()


@register.function 
def reaction_added(data):
    save_slack_data(data, ExampleSlackModel)
    print(data)
