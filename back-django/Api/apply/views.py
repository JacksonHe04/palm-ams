from django.db import IntegrityError
from django.shortcuts import render
from django.http import JsonResponse
from .models import Apply
from ..field.models import Field
from ..setting.models import University
from django.core.exceptions import ObjectDoesNotExist
import json
import uuid
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def apply_post(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            if not id:
                id = str(uuid.uuid4())
            print(id)

            # 获取所有字段定义
            fields = Field.objects.all()
            field_values = {}

            # 从请求数据中提取字段值
            for field in fields:
                field_values[field.variableName] = data.get(field.variableName)
            
            # 获取大学等级信息
            university_name = data.get('university')
            if university_name:
                try:
                    university = University.objects.get(name=university_name)
                    field_values['universityLevel'] = university.level
                except University.DoesNotExist:
                    # 如果找不到对应的大学，保持原值不变
                    pass

            # 获取硕士院校等级信息
            master_university_name = data.get('masterUniversity')
            if master_university_name:
                try:
                    master_university = University.objects.get(name=master_university_name)
                    field_values['masterUniversityLevel'] = master_university.level
                except University.DoesNotExist:
                    # 如果找不到对应的大学，保持原值不变
                    pass

            # 创建或更新 apply 对象
            apply_obj, created = Apply.objects.update_or_create(
                id=id,
                defaults=field_values
            )

            response_data = {
                'message': '申请表单提交成功',
                'data': {
                    'id': apply_obj.id,
                    'status': getattr(apply_obj, 'status', None)
                }
            }

            return JsonResponse(response_data, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def test_get(request):
    return JsonResponse({'message': 'This is a test GET request'})