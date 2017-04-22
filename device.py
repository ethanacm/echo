"""
a class to hold the various devices and their information we will need.
"""


class Device:
    def __init__(self, names, on_function, off_function, arg=None):
        self.names = names
        self.on_function = on_function
        self.off_function = off_function
        self.state = False
        self.arg = arg

    def get_state(self):
        return self.state

    def get_names(self):
        return self.names

    def get_primary_name(self):
        return self.names[0]

    def turn_on(self):
        if self.arg:
            self.on_function(self.arg)
        else:
            self.on_function()
        self.state = True

    def turn_off(self):
        self.off_function(self.arg)
        self.state = False











