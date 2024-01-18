from utils import api_utils
import json

# print(utils.get_slaves())

def group_filter():
    raw = api_utils.get_slaves()
    data = json.loads(raw)
    groups = []
    for i in data['data']:
        if 'chatroom' in i['wxid']:
            groups.append(i)
    return json.dumps(groups)

# print(group_filter())
print(api_utils.check_bot_login())