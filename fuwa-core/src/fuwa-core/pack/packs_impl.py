from ..pack.abstract_pack import AbstractPack
from ..contact.contact_impl import Contact, Group, Friend
from ..utils import api_utils

class C01SendMessagePack(AbstractPack):
    def __init__(self, message: str, to: Contact):
        super().__init__('C01SendMessagePack')
        self.message = message
        self.to = to

    def send(self):
        api_utils.send_msg(self.to.wxid, self.message)

class C02AddFriendPack(AbstractPack):
    def __init__(self, to: Contact, remark: str = None, verify_msg: str = ''):
        super().__init__('C02AddFriendPack')
        self.to = to
        self.remark = remark
        self.verify_msg = verify_msg

class C03AcceptFriendPack(AbstractPack):
    def __init__(self, from_: Contact):
        super().__init__('C03AcceptFriendPack')
        self.from_ = from_

class C04RemoveFriendPack(AbstractPack):
    def __init__(self, to: Contact):
        super().__init__('C04RemoveFriendPack')
        self.to = to

