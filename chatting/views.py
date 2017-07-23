from django.shortcuts import render
from django.http import HttpResponse
from .setting import user_profiles,LOCK_MESSAGE,RESTORE_MESSAGE
from channels import Group
import json
from chatting.auth_sdk import *
from .setting import sKey,iKey,api_host,random,auth_url
# from chatting.auth_sdk import *


def login_page(request):
    return render(request,"chatting/login.html")

def do_login(request):
    user = request.POST['user']
    passwd = request.POST['passwd']

    if not user or user not in user_profiles:
        return render(request,'chatting/failed.html')
    elif user_profiles[user] != passwd:
        return render(request,'chatting/failed.html')
    else:
        request.method = 'GET'
        # return render(request,"chatting/chatroom.html")
        return cm_auth(request,user)


def lock(request,user_name):
    Group(user_name).send({
        "text":json.dumps({
            "type":LOCK_MESSAGE
        })
    })

def restore(request,user_name):
    Group(user_name).send({
        "text":json.dumps({
            "type":RESTORE_MESSAGE
        })
    })



def auth_redirect(request):
    return render(request,"chatting/chatroom.html")


def cm_auth(request,user_name):
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
            context = {
                'auth_url': auth_url,
                'host': api_host
            }
            return render(request,"chatting/chatroom.html",context)

def test(request,user_name):
    context = {
        'auth_url': auth_url,
        'host':api_host
    }
    return render(request,"chatting/chatroom.html",context)
