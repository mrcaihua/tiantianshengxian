#coding=utf-8
from django.shortcuts import redirect

def user_login(func):
    def func1(request,*args,**kwargs):
        if request.session.has_key('uid'):
            #登陆成功
            return func(request,*args,**kwargs)
        else:
            #登陆失败
            return redirect('/ttsx_user/login/')
    return func1




