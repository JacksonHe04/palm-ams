from django.contrib import admin
from Api.apply.models import Apply

@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'applicationType', 'year', 'university', 'major', 'status']  # 在列表中显示的字段
    search_fields = ['name', 'university', 'major']  # 可搜索的字段
    list_filter = ['applicationType', 'year', 'status']  # 过滤器
