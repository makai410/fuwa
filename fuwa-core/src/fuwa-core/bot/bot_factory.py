class Bot:
    def __init__(
        self,
        account: str,
        city: str,
        name: str,
        wxid: str,
        mobile: str,
        signature: str
    ) -> None:
        self.account = account
        self.city = city
        self.name = name
        self.wxid = wxid
        self.mobile = mobile
        self.signature = signature

class BotFactory:
    def __init__(self) -> None:
        pass
    
    def create_bot():
        pass