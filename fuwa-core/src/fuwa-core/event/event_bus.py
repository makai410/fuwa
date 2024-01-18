from collections import defaultdict

class EventBus:
    def __init__(self):
        self._events = defaultdict(set)