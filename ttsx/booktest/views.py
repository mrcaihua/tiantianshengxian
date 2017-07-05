from django.shortcuts import render


def index(request):
    return render(request,'')

def register(request):
    return render(request,'register.html')