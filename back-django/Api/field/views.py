from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import Field
import json

@csrf_exempt
def get_field_list(request):
    if request.method == 'GET':
        fields = Field.objects.all()
        return JsonResponse([field.to_dict() for field in fields], safe=False)
    return JsonResponse({'error': '不支持的请求方法'}, status=405)

@csrf_exempt
def add_field(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            field = Field.objects.create(
                name=data['name'],
                description=data['description'],
                type=data.get('type', 'string'),
                variableName=data.get('variableName', ''),
                showInTable=data.get('showInTable', True),
                showInFilter=data.get('showInFilter', True),
                showInApply=data.get('showInApply', True),
                showInRecommendMaster=data.get('showInRecommendMaster', True),
                showInExamMaster=data.get('showInExamMaster', True),
                showInPhd=data.get('showInPhd', True),
                showInDirectPhd=data.get('showInDirectPhd', True),
                regionInForm=data.get('regionInForm', '其他')
            )
            return JsonResponse(field.to_dict())
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': '不支持的请求方法'}, status=405)

@csrf_exempt
def update_field(request, field_id):
    if request.method == 'PUT':
        try:
            field = Field.objects.get(id=field_id)
            data = json.loads(request.body)
            
            field.name = data.get('name', field.name)
            field.description = data.get('description', field.description)
            field.type = data.get('type', field.type)
            field.variableName = data.get('variableName', field.variableName)
            field.showInTable = data.get('showInTable', field.showInTable)
            field.showInFilter = data.get('showInFilter', field.showInFilter)
            field.showInApply = data.get('showInApply', field.showInApply)
            field.showInRecommendMaster = data.get('showInRecommendMaster', field.showInRecommendMaster)
            field.showInExamMaster = data.get('showInExamMaster', field.showInExamMaster)
            field.showInPhd = data.get('showInPhd', field.showInPhd)
            field.showInDirectPhd = data.get('showInDirectPhd', field.showInDirectPhd)
            field.regionInForm = data.get('regionInForm', field.regionInForm)
            
            field.save()
            return JsonResponse(field.to_dict())
        except ObjectDoesNotExist:
            return JsonResponse({'error': '字段不存在'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': '不支持的请求方法'}, status=405)

@csrf_exempt
def delete_field(request, field_id):
    if request.method == 'DELETE':
        try:
            field = Field.objects.get(id=field_id)
            field.delete()
            return JsonResponse({'message': '删除成功'})
        except ObjectDoesNotExist:
            return JsonResponse({'error': '字段不存在'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': '不支持的请求方法'}, status=405)