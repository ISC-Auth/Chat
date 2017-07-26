from channels import route
from .chat_consumers import *
from .behavior_consumer import *

chat_websocket_path = r"^/chatting/(?P<user_name>[a-zA-Z0-9]+)$"
behavior_auth_path = r"^/behavior/$"


general_routing = [
    route("websocket.connect",chat_connect,path=chat_websocket_path),
    route("websocket.receive",chat_message,path=chat_websocket_path),
    route("websocket.disconnect",chat_disconnect,path=chat_websocket_path),
    route("websocket.connect",be_connect,path=behavior_auth_path),
    route("websocket.receive",be_message,path=behavior_auth_path),
    route("websocket.disconnect",be_disconnect,path=behavior_auth_path),
]
