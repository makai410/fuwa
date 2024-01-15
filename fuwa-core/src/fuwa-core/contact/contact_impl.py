from collections import defaultdict
class Contact:
    __slots__ = ('wxid', )
    def __init__(self, wxid: str) -> None:
        self.wxid = wxid

class GroupMember(Contact):
    def __init__(self, wxid: str) -> None:
        super().__init__(wxid)

class Group(Contact):
    __slots__ = ('_members', )
    def __init__(self, chatroom_id: str) -> None:
        super().__init__(chatroom_id)
        self._members = defaultdict(GroupMember)

class Friend(Contact):
    __slots__ = ('wxid', )
    def __init__(self, wxid: str) -> None:
        super().__init__(wxid)
        self.wxid = wxid

class Message:
    def __init__(self, msg_id: str) -> None:
        self.msg_id = msg_id
