from channels import Group
from .setting import top_group_name,CHAT_MESSAGE
import json




def ws_connect(message,user_name):
    message.reply_channel.send({'accept':True})
    Group(top_group_name).add(message.reply_channel)
    Group(user_name).add(message.reply_channel)

def ws_message(message,user_name):
    Group(top_group_name).send({
        "text":json.dumps(
            {"type":CHAT_MESSAGE,
            "sender":user_name,
            "content":message['text']}
        ),
    })


def ws_disconnect(message,user_name):
    Group(top_group_name).discard(message.reply_channel)
    Group(user_name).discard(message.reply_channel)
    