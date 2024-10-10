from main import Command

class PowerCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a ** self.b

def load():
    return {'power': PowerCommand}
