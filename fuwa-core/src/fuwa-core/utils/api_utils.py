import requests
ADDRESS = 'http://127.0.0.1:19088/api' # wxhelper default port

def route(rt: str) -> str:
    return f'{ADDRESS}{rt}'

def get_bot_info() -> str:
    return requests.post(url=route('/userInfo')).text

def check_bot_login() -> str:
    return requests.post(url=route('/checkLogin')).text

def send_msg(wxid: str,
             msg: str = '') -> str:
    return requests.post(url=route('/sendTextMsg'),
                         data={
                             'wxid':wxid,
                             'msg':msg
                         }).text

def enable_sync_msg(port: str,
                    ip: str,
                    url: str = '',
                    timeout: str = '3000',
                    enable_http: bool = False) -> str:
    return requests.post(url=route('/hookSyncMsg'),
                         data={
                             'port':port,
                             'ip':ip,
                             'url':url,
                             'timeout':timeout,
                             'enableHttp':enable_http
                         }).text
    
def disable_sync_msg() -> str:
    return requests.post(url=route('/unhookSyncMsg')).text

def get_slaves() -> str:
    return requests.post(url=route('/getContactList')).text

def get_dbinfo() -> str:
    return requests.post(url=route('/getDBInfo')).text

def exec_sql(dbhandle: int,
             sql: str) -> str:
    return requests.post(url=route('/execSql'),
                         data={
                             'dbHandle':dbhandle,
                             'sql':sql
                         }).text

def lock_wechat() -> str:
    return requests.post(url=route('/lockWeChat')).text

def unlock_wechat() -> str:
    return requests.post(url=route('/unlockWeChat')).text

def click_enter_wechat() -> str:
    return requests.post(url=route('/clickEnterWeChat')).text

def forward_msg(wxid: str,
                msgid: str = '') -> str:
    return requests.post(url=route('/forwardMsg'),
                         data={
                             'wxid':wxid,
                             'msgId':msgid
                             }).text

def send_image(wxid: str,
               image_path: str) -> str:
    return requests.post(url=route('/sendImagesMsg'),
                         data={
                             'wxid':wxid,
                             'imagePath':image_path
                         }).text

def send_file(wxid: str,
              file_path: str) -> str:
    return requests.post(url=route('/sendFileMsg'),
                         data={
                             'wxid':wxid,
                             'filePath':file_path
                         }).text

def send_at(chatroom_id: str,
            wxids: str = 'notify@all', # split each wxid by ","
            msg: str = '') -> str:
    return requests.post(url=route('/sendAtText'),
                         data={
                             'wxids':wxids,
                             'chatRoomId':chatroom_id,
                             'msg':msg
                         }).text

def send_multi_at(chatroom_id: str,
                  at: list) -> str:
    return requests.post(url=route('/sendMultiAtText'),
                         data={
                             'chatRoomId':chatroom_id,
                             'at':at
                             }).text

def get_login_url() -> str:
    return requests.post(url=route('/getLoginUrl')).text

def translate_voice(msgid: str) -> str:
    return requests.post(url=route('/translateVoice'),
                         data={
                             'msgId':msgid
                         }).text
def get_translate_voice_text(msgid: str) -> str:
    return requests.post(url=route('/getTranslateVoiceText'),
                         data={
                             'msgId':msgid
                         }).text