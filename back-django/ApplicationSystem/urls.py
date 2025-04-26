# Application/urls.py
"""
路由管理器，根据网址匹配到对应的视图函数
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
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
    path('api/date/', include('Api.date.urls')),  # 添加 date 应用的路由

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
