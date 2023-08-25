import requests

def convert(message):
    sign = {"&": "%26", "+": "%2B", "#": "%23"}
    for i in sign:
        message = message.replace(i, sign[i]) #防止在请求中特殊符号出现消息错误
    return message

def sendGroup(uid, gid, message):
    '''群消息'''
    message = convert(message)
    message = "[CQ:at,qq={}]\n".format(uid) + message #CQ码，这里是at某人的作用
    requests.get(
        url = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, message)
    )

def sendPrivate(uid, message):
    '''私聊消息'''
    message = convert(message)
    requests.get(
        url = 'http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid, message)
    )
