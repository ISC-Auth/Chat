from channels import Group
from .setting import chat_top_group_name,CHAT_MESSAGE
import json




def chat_connect(message,user_name):
    message.reply_channel.send({'accept':True})
    print('in conncect',user_name)
    Group(chat_top_group_name).add(message.reply_channel)
    Group(user_name).add(message.reply_channel)

def chat_message(message,user_name):
    Group(chat_top_group_name).send({
        "text":json.dumps(
            {"type":CHAT_MESSAGE,
            "sender":user_name,
            "content":message['text']}
        ),
    })


def chat_disconnect(message,user_name):
    Group(chat_top_group_name).discard(message.reply_channel)
    Group(user_name).discard(message.reply_channel)