from enum import Enum, unique

@unique
class Identity(Enum):
    Client = 'Client'
    Admin = 'Admin'
    Owner = 'Owner'

class Contact():
    def __init__(self, name: str, wxid: str):
        self.name = name
        self.wxid = wxid

class Friend(Contact):
    def __init__(self, name: str, wxid: str, identity: Identity):
        super(Friend, self).__init__(name, wxid)
        self.identity = identity


class Group(Contact):
    def __init__(self, name: str, wxid: str, members: dict):
        super(Group, self).__init__(name, wxid)
        self.members = members