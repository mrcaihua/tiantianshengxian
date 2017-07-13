#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
from models import *
from hashlib import sha1
import datetime
from user_decorators import *

# Create your views here.
def register(request):
    context={'title':'注册','top':'0'}
    return render(request,'ttsx_user/register.html',context)


def register_handle(request):
    s1=sha1()
    #获取post对象
    post=request.POST
    uname=post.get('user_name')
    upwd=post.get('user_pwd')
    umail=post.get('user_email')
    #对密码进行加密
    s1.update(upwd)
    #获取加密后的密码
    result=s1.hexdigest()
    user_info=UserInfo()
    user_info.uname=uname
    user_info.upwd=result
    user_info.umail=umail
    user_info.save()
    return redirect('/ttsx_user/login/')


def register_valid(request):
    uname=request.GET.get('uname')
    result=UserInfo.objects.filter(uname=uname).count()
    context={'valid':result}
    return JsonResponse(context)


def login(request):
    uname=request.COOKIES.get('uname','')
    print uname
    context={'title':'登陆','uname':uname,'top':'0'}
    return render(request,'ttsx_user/login.html',context)


def login_handle(request):
    post=request.POST
    uname=post.get('user_name')
    upwd=post.get('user_pwd')
    uname_jz=post.get('name_jz', '0')

    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    context = {'title': '登陆', 'uname': uname, 'upwd': upwd, 'top':'0'}
    users=UserInfo.objects.filter(uname=uname)
    if len(users) == 0:
        #用户名错误
        context['name_error'] = '1'
        return render(request, 'ttsx_user/login.html', context)
    else:
        #登陆成功
        if users[0].upwd == upwd_sha1:
            #记住当前登陆的用户
            request.session['uid'] = users[0].id
            request.session['uname'] = uname
            #记住用户名
            path=request.session.get('url_path','/')
            response=redirect(path)
            if uname_jz=='1':
                response.set_cookie('uname',uname,expires=datetime.datetime.now() + datetime.timedelta(days = 7))
            else:
                response.set_cookie('uname','',max_age=-1)
            return response
        else:
            #密码错误
            context['pwd_error']='1'
        return render(request,'ttsx_user/login.html',context)


def logout(request):
    request.session.flush()
    return redirect('/ttsx_user/')

@user_login
def center(request):
    user=UserInfo.objects.get(pk=request.session['uid'])

    context={'title':'用户中心','user':user}
    return render(request,'ttsx_user/center.html',context)

@user_login
def order(request):
    context = {'title':'用户订单'}
    return render(request, 'ttsx_user/order.html', context)

@user_login
def site(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    if request.method=='POST':
        post=request.POST
        user.ushou=post.get('ushou')
        user.addrss=post.get('uaddrss')
        user.uphone=post.get('uphone')
        user.ucode=post.get('ucode')
        user.save()
    context = {'title':'用户地址','user':user}
    return render(request, 'ttsx_user/site.html', context)




