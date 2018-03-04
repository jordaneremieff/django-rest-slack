class Registry:

    """
    Register functions for handling Slack events and commands.
    """

    def __init__(self):
        self.functions = {}

    def function(self, func):
        if callable(func):
            self.functions[func.__name__] = func
            return func

    def get_function(self, name):
        func = self.functions.get(name)
        if not func:
            raise ValueError('{} is not a registered Slack function.'.format(func))
        return func
