from django.db import IntegrityError
from django.shortcuts import render
from django.http import JsonResponse
from .models import Apply
from ..field.models import Field
from django.core.exceptions import ObjectDoesNotExist
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def apply_post(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            print(id)

            # 获取所有字段定义
            fields = Field.objects.all()
            field_values = {}

            # 从请求数据中提取字段值
            for field in fields:
                field_values[field.variableName] = data.get(field.variableName)

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