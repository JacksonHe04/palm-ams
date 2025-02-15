# Application/urls.py
"""
路由管理器，根据网址匹配到对应的视图函数
"""
from django.contrib import admin
from django.urls import path, include
from . import testdb
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('management/', admin.site.urls), # Django的Admin页面


    # path('', views.process_form),
    # path('', include('apply.urls')),
    # path('apply_old/', views.process_form_old),
    # path('old/', views.index_old),
    path('testdb/', testdb.testdb),

    path('api/test/', include('Api.testapp.urls',)),
    # path('api/front-desk/', include('Api.front-desk.urls',)),
    path('api/apply/',include('Api.apply.urls',)),
    path('api/students/', include('Api.students.urls',)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
