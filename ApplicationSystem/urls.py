# Application/urls.py
"""
路由管理器，根据网址匹配到对应的视图函数
"""
from django.contrib import admin
from django.urls import path
from Apply import views
from . import testdb
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apply/',views.palm),
    path('testdb/', testdb.testdb),
    path('', views.index),
    path('vue/', views.indexVue)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
