# Application/urls.py
"""
路由管理器，根据网址匹配到对应的视图函数
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # API路由
    path('api/apply/',include('Api.apply.urls',)),
    path('api/students/', include('Api.students.urls',)),
    path('api/auth/', include('Api.auth.urls',)),
    path('api/settings/', include('Api.setting.urls')),
    path('api/filter/', include('Api.filter.urls',)),
    path('api/test/', include('Api.testapp.urls',)),
    path('api/field/', include('Api.field.urls',)),
    path('api/percent/', include('Api.percent.urls',)),
    path('api/result/', include('Api.result.urls',)),
    path('api/files/', include('Api.files.urls',)),
    path('api/interview/', include('Api.interview.urls',)),
    path('api/date/', include('Api.date.urls')),

    # 所有非API的路由都交给前端处理
    re_path(r'^.*$', views.index, name='index'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
