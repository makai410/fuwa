from enum import Enum

class Event:
    __slots__ = ('_name', )
    def __init__(self, name: str) -> None:
        self._name = name
    
    @property
    def name(self) -> str:
        return self._name

class MessageType(Enum):
    Text = 0,
    File = 1,
    Image = 2,
    At = 3

class Toggle(Enum):
    ENABLE = 0,
    DISABLE = 1

class SendMessageEvent(Event):
    __slots__ = ('_type', )
    def __init__(self, type: MessageType) -> None:
        super().__init__('SendMessageEvent')
        self._type = type

    @property
    def type(self) -> MessageType:
        return self._type

class LoginEvent(Event):
    def __init__(self) -> None:
        super().__init__('LoginEvent')

class AddFriendEvent(Event):
    def __init__(self) -> None:
        super().__init__('AddFriendEvent')

class DeleteFriendEvent(Event):
    def __init__(self) -> None:
        super().__init__('DeleteFriendEvent')

class HookerEvent(Event):
    __slots__ = ('_type', )
    def __init__(self, type: Toggle) -> None:
        super().__init__('HookerEvent')
        self._type = type
