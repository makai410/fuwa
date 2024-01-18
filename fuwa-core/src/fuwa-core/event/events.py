from ..pack.abstract_pack import AbstractPack
class Event:
    def __init__(self, name):
        self.name = name

class SendPackEvent(Event):
    def __init__(self, pack: AbstractPack):
        self.pack = pack