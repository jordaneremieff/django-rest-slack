from importlib import import_module

from django.apps import apps


def get_slack_registry():
    registry = {}
    app_module_names = ['{}.slack_functions'.format(app_config.name) for app_config in apps.get_app_configs()]
    for app_module_name in app_module_names:
        try:
            app_module = import_module(app_module_name)
        except ImportError:
            continue
        registry[app_module_name] = app_module.register
    return registry


def get_slack_function(func_name):
    registry = get_slack_registry()
    func = None
    if registry:
        for app_file, app_registry in registry.items():
            func = app_registry.get_function(func_name)
    return func


def save_slack_data(data, model_class):
    try:
        data['command']
        type = model_class.COMMAND
    except KeyError:
        type = model_class.EVENT
    model_class.objects.create(type=type, data=data)
