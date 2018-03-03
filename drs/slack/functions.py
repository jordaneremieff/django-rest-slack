from .models import SlackModel

def save_data(data):
    try:
        data['command']
        type = SlackModel.COMMAND
    except KeyError:
        type = SlackModel.EVENT
    SlackModel.objects.create(type=type, data=data)


def example_event(data):
    # Handle the event
    # Save the data
    save_data(data)
    # We don't return anything here


def example_command(data):
    # Handle the slash command
    # Save the data
    save_data(data)
    return {"response_type": "ephemeral", "text": "You did a thing"}
