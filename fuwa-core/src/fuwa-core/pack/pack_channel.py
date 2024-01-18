from ..pack.packs_impl import *
from ..pack.abstract_pack import AbstractPack
import threading
import taichi as ti

class DataPackChannel:
    def __init__(self):
        self._channel_thread = threading.Thread(target=self._exec)
        self.pack_queue = [AbstractPack]
        self._channel_thread.setDaemon(True)

    def _exec(self):
        while True:
            pack = self._listen_pack_queue()
            if pack is None:
                continue
            self.send_pack(pack)

    def _listen_pack_queue(self):
        if len(self.pack_queue) > 0:
            return self.pack_queue.pop(0)
        return None

    def start(self):
        self._channel_thread.start()

    def send_pack(self, data: AbstractPack):
        pass