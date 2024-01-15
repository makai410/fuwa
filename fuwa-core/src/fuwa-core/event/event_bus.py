from functools import wraps
from threading import Thread
from collections import defaultdict, Counter
from typing import Iterable, Callable, List, Dict, Any, Set, Union

from ..event.exceptions import EventDoesntExist
from ..event.events import *

class EventBus:
    __slots__ = ('_events',)
    
    def __init__(self) -> None:
        self._events = defaultdict(set)  # type: Dict[Any, Set[Callable]]

    def __repr__(self) -> str:
        return "<{}: {} subscribed events>".format(
            self.cls_name,
            self.event_count
        )

    def __str__(self) -> str:
        return "{}".format(self.cls_name)

    @property
    def event_count(self) -> int:
        return self._subscribed_event_count()

    @property
    def cls_name(self) -> str:
        return self.__class__.__name__

    def listen(self, event: Event) -> Callable:
        def outer(func):
            self.add_event(func, event.name)
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper

        return outer

    def add_event(self, func: Callable, event: Event) -> None:
        self._events[event.name].add(func)

    def emit(self, event: Event, *args, **kwargs) -> None:
        threads = kwargs.pop('threads', None)

        if threads:
            events = [
                Thread(target=f, args=args, kwargs=kwargs) for f in
                self._event_funcs(event)
            ]

            for event in events:
                event.start()
        else:
            for func in self._event_funcs(event):
                func(*args, **kwargs)

    def emit_only(self, event: Event, func_names: Union[str, List[str]], *args,
                  **kwargs) -> None:
        if isinstance(func_names, str):
            func_names = [func_names]

        for func in self._event_funcs(event):
            if func.__name__ in func_names:
                func(*args, **kwargs)

    def emit_after(self, event: Event) -> Callable:
        def outer(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                returned = func(*args, **kwargs)
                self.emit(event)
                return returned

            return wrapper

        return outer

    def remove_event(self, func_name: str, event: Event) -> None:
        event_funcs_copy = self._events[event.name].copy()

        for func in self._event_funcs(event):
            if func.__name__ == func_name:
                event_funcs_copy.remove(func)

        if self._events[event.name] == event_funcs_copy:
            err_msg = "function doesn't exist inside event {} ".format(event)
            raise EventDoesntExist(err_msg)
        else:
            self._events[event.name] = event_funcs_copy

    def _event_funcs(self, event: Event) -> Iterable[Callable]:
        for func in self._events[event.name]:
            yield func

    def _event_func_names(self, event: Event) -> List[str]:
        return [func.__name__ for func in self._events[event.name]]

    def _subscribed_event_count(self) -> int:
        event_counter = Counter()  # type: Dict[Any, int]

        for key, values in self._events.items():
            event_counter[key] = len(values)

        return sum(event_counter.values())