import requests
ADDRESS = '127.0.0.1:19088/api/'

def route(rt: str) -> str:
    return f'{ADDRESS}{rt}'

def post_request(rt: str, data=None):
    return requests.post(
        url=route(rt),
        data=data
    ).json()

def check_login():
    return post_request(
        rt='checkLogin'
    )

def get_bot_info():
    return post_request(
        rt='userInfo'
    )

def send_text_msg(wxid: str, msg: str = ''):
    return post_request(
        rt='sendTextMsg',
        data=locals()
    )

def enable_hooker(
    ip: str = '127.0.0.1',
    port: str = '11451',
    url: str = 'http://127.0.0.1:11451',
    timeout: str = '3000',
    enableHttp: bool = True
):
    return post_request(
        rt='hookSyncMsg',
        data=locals()
    )

def disable_hooker():
    return post_request(
        rt='unhookSyncMsg'
    )

def get_contact_list():
    return post_request(
        rt='getContactList'
    )

def get_dbinfo():
    return post_request(
        rt='getDBInfo'
    )

def exec_sql(dbHandle: int, sql: str):
    return post_request(
        rt='execSql',
        data=locals()
    )

def send_img(wxid: str, imagePath: str):
    return post_request(
        rt='sendImagesMsg',
        data=locals()
    )

def send_file(wxid: str, filePath: str):
    return post_request(
        rt='sendFileMsg',
        data=locals()
    )

def send_at_msg(wxids: str, chatRoomId: str, msg: str):
    return post_request(
        rt='sendAtText',
        data=locals()
    )

def send_multi_at_msg(chatRoomId: str, at: list(dict)):
    return post_request(
        rt='sendMultiAtText',
        data=locals()
    )

def get_login_url():
    return post_request(
        rt='getLoginUrl'
    )

def translate_voice(msgId: str):
    return post_request(
        rt='translateVoice',
        data=locals()
    )

def get_voice_text(msgId: str):
    return post_request(
        rt='getTranslateVoiceText',
        data=locals()
    )

