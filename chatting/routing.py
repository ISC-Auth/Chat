
from channels import route
from .consumers import ws_connect,ws_message,ws_disconnect

websocket_path = r"^/chatting/(?P<user_name>[a-zA-Z0-9]+)$"
general_routing = [
    route("websocket.connect",ws_connect,path=websocket_path),
    route("websocket.receive",ws_message,path=websocket_path),
    route("websocket.disconnect",ws_disconnect,path=websocket_path)
]