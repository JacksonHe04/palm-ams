from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import FilterScheme
from .serializers import FilterSchemeSerializer
from Api.apply.models import Apply
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from ..auth.views import jwt_auth_required

class FilterSchemeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FilterScheme.objects.all()
    serializer_class = FilterSchemeSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'success': False,
                'message': '创建筛选方案失败'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'success': False,
                'message': '更新筛选方案失败'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return Response({
                'success': False,
                'message': '删除筛选方案失败'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def apply(self, request):
        try:
            filter_config = request.data.get('config', {})
            query = Q()

            for field, conditions in filter_config.items():
                operator = conditions.get('operator')
                value = conditions.get('value')
                
                if value is None or value == '':
                    continue

                if operator == 'contains':
                    query &= Q(**{f"{field}__icontains": value})
                elif operator == 'equals':
                    query &= Q(**{field: value})
                elif operator == 'startsWith':
                    query &= Q(**{f"{field}__istartswith": value})
                elif operator == 'endsWith':
                    query &= Q(**{f"{field}__iendswith": value})
                elif operator == 'gt':
                    query &= Q(**{f"{field}__gt": value})
                elif operator == 'lt':
                    query &= Q(**{f"{field}__lt": value})
                elif operator == 'eq':
                    query &= Q(**{field: value})
                elif operator == 'neq':
                    query &= ~Q(**{field: value})

            filtered_results = Apply.objects.filter(query)
            results = [
                {
                    'id': item.id,
                    'name': item.name,
                    'university': item.university,
                    'major': item.major,
                    'status': item.status,
                    # 添加其他需要返回的字段
                }
                for item in filtered_results
            ]

            return Response({
                'success': True,
                'data': results
            })
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@jwt_auth_required
@require_http_methods(["GET", "POST"])
def filter_schemes(request):
    if request.method == "GET":
        schemes = FilterScheme.objects.all().values()
        return JsonResponse({
            'success': True,
            'data': list(schemes)
        })
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            scheme = FilterScheme.objects.create(
                name=data['name'],
                fields=data['fields'],
                config=data['config']
            )
            return JsonResponse({
                'success': True,
                'message': '方案保存成功',
                'data': {
                    'id': scheme.id,
                    'name': scheme.name,
                    'fields': scheme.fields,
                    'config': scheme.config
                }
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=400) 