from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from .models import Percent
import json

@csrf_exempt
@require_http_methods(['GET'])
def get_percent(request):
    try:
        # 获取第一条记录，如果不存在则创建
        percent, created = Percent.objects.get_or_create(id=1)
        data = {
            'pOfA': percent.pOfA or 0,
            'pOfB': percent.pOfB or 0,
            'pOfC': percent.pOfC or 0,
            'pOfATop': percent.pOfATop or 0,
            'pOfBTop': percent.pOfBTop or 0,
            'pOfCTop': percent.pOfCTop or 0,
            'pOfATalent': percent.pOfATalent or 0,
            'pOfBTalent': percent.pOfBTalent or 0,
            'pOfCTalent': percent.pOfCTalent or 0
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(['PUT'])
def update_percent(request, pk):
    try:
        data = json.loads(request.body)
        percent = Percent.objects.get(id=pk)
        
        # 更新所有字段
        percent.pOfA = data.get('pOfA', percent.pOfA)
        percent.pOfB = data.get('pOfB', percent.pOfB)
        percent.pOfC = data.get('pOfC', percent.pOfC)
        percent.pOfATop = data.get('pOfATop', percent.pOfATop)
        percent.pOfBTop = data.get('pOfBTop', percent.pOfBTop)
        percent.pOfCTop = data.get('pOfCTop', percent.pOfCTop)
        percent.pOfATalent = data.get('pOfATalent', percent.pOfATalent)
        percent.pOfBTalent = data.get('pOfBTalent', percent.pOfBTalent)
        percent.pOfCTalent = data.get('pOfCTalent', percent.pOfCTalent)
        
        percent.save()
        
        # 返回更新后的数据
        return JsonResponse({
            'pOfA': percent.pOfA,
            'pOfB': percent.pOfB,
            'pOfC': percent.pOfC,
            'pOfATop': percent.pOfATop,
            'pOfBTop': percent.pOfBTop,
            'pOfCTop': percent.pOfCTop,
            'pOfATalent': percent.pOfATalent,
            'pOfBTalent': percent.pOfBTalent,
            'pOfCTalent': percent.pOfCTalent
        })
    except ObjectDoesNotExist:
        return JsonResponse({'error': '记录不存在'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': '无效的JSON数据'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)