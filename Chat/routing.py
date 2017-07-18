from channels import include


channel_routing = [
    include("chatting.routing.general_routing",path="^")
    # include("isc_auth.routing.general_routing",path="^"),
    # include("isc_auth.routing.custom_routing",path="^"),
]