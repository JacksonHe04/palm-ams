from django.db import IntegrityError
from django.shortcuts import render
from django.http import JsonResponse
from .models import TestStudent
from django.core.exceptions import ObjectDoesNotExist
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  # 若启用了 CSRF 保护，需要禁用此视图的 CSRF 检查
def test_post(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # 将 JSON 请求体解析为字典
            name = data.get('name')
            age = data.get('age')
            grade = data.get('grade')

            # 检查数据有效性
            if not name or not age or not grade:
                return JsonResponse({'status': 'error', 'message': '缺少必要参数'}, status=400)

            # 创建并保存新学生记录
            new_student = TestStudent(name=name, age=age, grade=grade)
            new_student.save()
            return JsonResponse({'status': 'success', 'message': '学生信息提交成功'}, status=201)
        except IntegrityError as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': '请求方法错误'}, status=400)


def test_get(request):
    if request.method == 'GET':
        # 获取前端传递的学生姓名
        name = request.GET.get('name')

        try:
            # 尝试从数据库中获取学生信息
            student = TestStudent.objects.get(name=name)
            # 构建响应数据
            data = {
                'name': student.name,
                'age': student.age,
                'grade': student.grade
            }
            return JsonResponse({'status': 'success', 'data': data})
        except ObjectDoesNotExist:
            # 如果没有找到学生，则返回错误信息
            return JsonResponse({'status': 'error', 'message': '未找到该学生信息'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': '请求方法错误'}, status=400)
