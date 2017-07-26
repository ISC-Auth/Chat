from django.shortcuts import render
from django.http import HttpResponse
from chatting.auth_sdk import *
from channels import Group
from .behavior_setting import behavior_chat_group_name,RESTORE_MESSAGE


sKey = "8UFCjZNCu2rtiZhhGeonFtwudpzmXITN48FcbUEj"
iKey = "iaN5VI6U1jphHvPAnzGC"
random = "mBMayeaovwGVwuXFUmExdtUy8bABVbsWViS61zON"
api_host = "api-IC8aOYgD"



def news_cm_auth(request,user_name):
    if request.method == "GET":
        sig_request = sign_request(iKey,sKey,random,user_name)
        context = {
            'post_action':'http://'+ request.get_host() +'/login_/{}/'.format(user_name),
            'sig_request':sig_request,
            'host':api_host
        }
        return render(request,"chatting/second_login.html",context)

    elif request.method == "POST":
        sig_response = request.POST.get('sig_response', '')
        cm_user = verify_response(iKey,sKey,random,sig_response)
        if cm_user is None:
            return HttpResponse('Failed Second Login')
        else:    
            Group(behavior_chat_group_name).send({"text":RESTORE_MESSAGE})
            return HttpResponse('Succeed')









