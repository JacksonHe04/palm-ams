from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from .models import AdmissionDate
from .serializers import AdmissionDateSerializer

class AdmissionDateViewSet(viewsets.ModelViewSet):
    """
    招生时间配置视图集
    """
    queryset = AdmissionDate.objects.all()
    serializer_class = AdmissionDateSerializer

    def get_queryset(self):
        """
        根据年份筛选数据
        """
        queryset = AdmissionDate.objects.all()
        # 优先从 URL 路径参数获取年份
        year = self.kwargs.get('pk')
        # 如果路径参数中没有，则尝试从查询参数获取
        if not year:
            year = self.request.query_params.get('year')
        if year is not None:
            queryset = queryset.filter(year=year)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        """
        获取单个年份的招生时间配置
        如果不存在则创建默认记录
        """
        year = kwargs.get('pk')
        queryset = self.get_queryset()
        
        if not queryset.exists():
            admission_types = ['推免硕士', '考研硕士', '博士', '直博']
            for type_name in admission_types:
                AdmissionDate.objects.create(
                    year=year,
                    type=type_name,
                    start_time=None,
                    end_time=None
                )
            queryset = AdmissionDate.objects.filter(year=year)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def update_year(self, request, pk=None):
        """
        更新指定年份的招生时间配置
        """
        year = pk
        if not year:
            return Response({'error': '年份参数缺失'}, status=status.HTTP_400_BAD_REQUEST)

        dates = request.data
        if not isinstance(dates, list):
            return Response({'error': '数据格式错误'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                # 删除该年份的所有记录
                AdmissionDate.objects.filter(year=year).delete()
    
                # 转换字段名
                processed_dates = []
                for date in dates:
                    processed_date = {
                        'year': year,
                        'type': date['type'],
                        'start_time': date.get('start_time'),  # 从 startTime 获取值
                        'end_time': date.get('end_time')       # 从 endTime 获取值
                    }
                    processed_dates.append(processed_date)
    
                # 创建新记录
                serializer = self.get_serializer(data=processed_dates, many=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
    
                return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)