#coding=utf-8
from django.shortcuts import render
from models import *
# Create your views here.
def index(request):

    context={'title':'首页'}
    return render(request,'ttsx_goods/index.html',context)