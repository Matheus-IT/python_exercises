class Smartphone():
    def __init__(self, n=0, inter=None):
        self.size = n
        self.interface = inter


class Mp3_player(Smartphone):
    def __init__(self):
        Smartphone.__init__(self)
        self.capacity = None
