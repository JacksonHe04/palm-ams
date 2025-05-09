from django.http import JsonResponse
from django.db import models
from django.core.exceptions import FieldDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from Api.apply.models import Apply
from Api.files.models import File
import json

def get_model_fields(model):
    """
    获取模型的所有字段信息，处理不可序列化的默认值
    """
    fields = []
    for field in model._meta.fields:
        default = field.default
        # 处理不可序列化的默认值
        if callable(default):
            default = None
        elif default == models.fields.NOT_PROVIDED:
            default = None
            
        field_info = {
            'name': field.name,
            'type': field.get_internal_type(),
            'null': field.null,
            'blank': field.blank,
            'default': default
        }
        fields.append(field_info)
    return fields

@csrf_exempt
def apply_data(request):
    """
    处理申请数据的视图函数
    支持 GET 和 POST 请求，实现增删改查功能
    """
    if request.method == 'GET':
        # 获取所有记录
        applies = Apply.objects.all()
        # 获取所有字段信息
        fields = get_model_fields(Apply)
        
        # 将查询集转换为列表
        applies_list = list(applies.values())
        
        return JsonResponse({
            'records': applies_list,
            'fields': fields
        })
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            action = data.get('action', 'create')
            
            if action == 'create':
                # 创建新记录
                apply = Apply.objects.create(**data['data'])
                return JsonResponse({'message': '创建成功', 'id': apply.id})
                
            elif action == 'update':
                # 更新记录
                Apply.objects.filter(id=data['id']).update(**data['data'])
                return JsonResponse({'message': '更新成功'})
                
            elif action == 'delete':
                # 删除记录
                Apply.objects.filter(id=data['id']).delete()
                return JsonResponse({'message': '删除成功'})
                
            else:
                return JsonResponse({'error': '不支持的操作'}, status=400)
                
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': '不支持的请求方法'}, status=405)

@csrf_exempt
def files_data(request):
    """
    处理文件相关的数据库操作
    支持 GET 和 POST 请求，实现增删改查功能
    """
    if request.method == 'GET':
        try:
            # 获取所有记录
            files = File.objects.filter(is_deleted=False)
            # 获取所有字段信息
            fields = get_model_fields(File)
            
            # 将查询集转换为列表
            files_list = list(files.values())
            
            return JsonResponse({
                'records': files_list,
                'fields': fields
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            action = data.get('action', 'create')
            
            if action == 'create':
                # 创建新记录
                file = File.objects.create(**data['data'])
                return JsonResponse({'message': '创建成功', 'id': file.id})
                
            elif action == 'update':
                # 更新记录
                File.objects.filter(id=data['id']).update(**data['data'])
                return JsonResponse({'message': '更新成功'})
                
            elif action == 'delete':
                # 删除记录
                file = File.objects.get(id=data['id'])
                file.delete()  # 使用模型的软删除方法
                return JsonResponse({'message': '删除成功'})
                
            else:
                return JsonResponse({'error': '不支持的操作'}, status=400)
                
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': '不支持的请求方法'}, status=405)
