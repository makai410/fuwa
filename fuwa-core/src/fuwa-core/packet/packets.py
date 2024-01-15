from ..contact.contact_impl import *
from ..utils.api_utils import *
from enum import Enum

class ResultType(Enum):
    SUCCESS = 1,
    FAIL = 0

class Packet:
    __slots__ = ('_name', )
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def parse(self): pass

class C00CheckLogin(Packet):
    def __init__(self) -> None:
        super().__init__('C00CheckLogin')

    def parse(self):
        return check_login()['code']

class C01GetBotInfo(Packet):
    def __init__(self) -> None:
        super().__init__('C01GetUserInfo')

    def parse(self):
        return get_bot_info()['data']

class C02SendTextMessage(Packet):
    def __init__(self, target: Contact, msg: str) -> None:
        super().__init__('C02SendTextMessage')
        self.target_wxid = target.wxid
        self.content = msg

    def parse(self):
        return send_text_msg(
            wxid=self.target_wxid,
            msg=self.content
        )['msg']

class C03EnableHookerTCP(Packet):
    def __init__(self, ip: str, port: str, timeout: str = '3000') -> None:
        super().__init__('C03EnableHookerTCP')
        self.ip = ip
        self.port = port
        self.timeout = timeout

    def parse(self):
        return enable_hooker(
            ip=self.ip,
            port=self.port,
            timeout=self.timeout,
            enableHttp=False   
        )['msg']

class C04EnableHookerHTTP(Packet):
    def __init__(self, url: str, timeout: str = '3000') -> None:
        super().__init__('C04EnableHookerHTTP')
        self.url = url
        self.timeout = timeout

    def parse(self):
        return enable_hooker(
            url=self.url,
            timeout=self.timeout
        )['msg']

class C05DisableHooker(Packet):
    def __init__(self) -> None:
        super().__init__('C05DisableHooker')

    def parse(self):
        return disable_hooker()['msg']

class C06GetContactList(Packet):
    def __init__(self) -> None:
        super().__init__('C06GetContactList')

    def parse(self):
        return get_contact_list()['data']

class C07SendImageMessage(Packet):
    def __init__(self, target: Contact, img_path: str) -> None:
        super().__init__('C07SendImageMessage')
        self.target_wxid = target.wxid
        self.img_path = img_path

    def parse(self):
        return send_img(
            wxid=self.target_wxid,
            imagePath=self.img_path
        )['msg']

class C08SendFileMessage(Packet):
    def __init__(self, target: Contact, file_path: str) -> None:
        super().__init__('C08SendFileMessage')
        self.target_wxid = target.wxid
        self.file_path = file_path

    def parse(self):
        return send_file(
            wxid=self.target_wxid,
            filePath=self.file_path
        )['msg']

class C09SendAtMessage(Packet):
    def __init__(self, group: Group, people: list[Friend], msg: str) -> None:
        super().__init__('C09SendAtMessage')
        self.target = group
        self.wxids = [p.wxid for p in people]
        self.msg = msg
    
    def parse(self):
        return send_at_msg(
            wxids=','.join(self.wxids),
            chatRoomId=self.target.wxid,
            msg=self.msg
        )
