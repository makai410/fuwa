from ..packet.packets import *
from threading import Thread

class PacketChannel:
    __slots__ = ('_queue', )
    def __init__(self) -> None:
        self._queue = [Packet]

    def _exec(self):
        while True:
            if not self._queue:
                continue
            # self._queue.pop(0)

    def stream(self):
        Thread(target=self._exec).start()

    def push(self, packet: Packet):
        self._queue.append(packet)