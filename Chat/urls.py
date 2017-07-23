
from django.conf.urls import url
from django.contrib import admin
from chatting.views import do_login,login_page,lock,restore,cm_auth

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^login/$',login_page,name="login_page"),
    url(r'^$',login_page,name="login_page"),
    url(r'^do_login/$',do_login,name="do_login"),
    url(r'^lock/(?P<user_name>[a-zA-Z0-9]+)/$',lock,name="lock"),
    url(r'^restore/(?P<user_name>[a-zA-Z0-9]+)/$',restore,name="restore"),
    url(r'^login_/(?P<user_name>[a-zA-Z0-9]+)/$',cm_auth,name="cm_auth")
]
