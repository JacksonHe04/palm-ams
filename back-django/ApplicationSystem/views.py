from django.shortcuts import render
from django.conf import settings
import os

def index(request):
    """
    渲染前端页面的入口函数
    用于服务前端 Vue 应用的 index.html
    """
    return render(request, 'index.html')

def login(request):
    return render(request, 'index.html')

def admin(request):
    return render(request, 'index.html')