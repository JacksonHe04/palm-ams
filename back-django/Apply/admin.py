# apply/management.py
"""
1. 显示申请者填写的字段
2. 提供导出选中数据到Excel文件的功能。
"""
from django.contrib import admin
from .models import PalmApplicant
from django.shortcuts import HttpResponse
from openpyxl import Workbook

class testAdmin(admin.ModelAdmin):
    list_display = ('name_input','sex_input','birthday','province','city','district','undergraduate_university_input')
    actions = ["export_excel",]

    def export_excel(self, request, queryset):
        meta = PalmApplicant._meta  
        field_names = [field.name for field in meta.fields]  # 模型所有字段名
        field_verbose_names = [field.verbose_name for field in meta.fields]  # 模型所有字段名

        response = HttpResponse(content_type='application/msexcel')  # 定义响应内容类型
        response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'  # 定义响应数据格式
        wb = Workbook()  # 新建Workbook
        ws = wb.active  # 使用当前活动的Sheet表
        ws.append(field_verbose_names)  # 将模型字段名作为标题写入第一行
        for obj in queryset:  # 遍历选择的对象列表
            for field in field_names:
                data = [f'{getattr(obj, field)}' for field in field_names]  # 将模型属性值的文本格式组成列表
            row = ws.append(data)  # 写入模型属性值
        wb.save(response)  # 将数据存入响应内容
        return response

    export_excel.short_description = "导出Excel文件"


admin.site.register(PalmApplicant,testAdmin)