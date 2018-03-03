from .models import SlackModel

def save_data(data):
    '''
    Save the slack data by type, command or event.
    '''
    try:
        data['command']
        type = SlackModel.COMMAND
    except KeyError:
        type = SlackModel.EVENT
    SlackModel.objects.create(type=type, data=data)


def example_event(data):
    '''
    Handle a particular event and save the data. 
    '''
    save_data(data)
    # We don't return anything here


def example_command(data):
    '''
    Handle a particular slash command and save the data.
    '''
    save_data(data)
    return {"response_type": "ephemeral", "text": "You did a thing"}
