from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import FilterScheme
from .serializers import FilterSchemeSerializer

class FilterSchemeViewSet(viewsets.ModelViewSet):
    queryset = FilterScheme.objects.all()
    serializer_class = FilterSchemeSerializer

    @action(detail=True, methods=['patch'])
    def toggle(self, request, pk=None):
        scheme = self.get_object()
        enabled = request.data.get('enabled')
        
        if enabled is None:
            return Response(
                {'error': '启用状态参数缺失'},
                status=status.HTTP_400_BAD_REQUEST
            )

        scheme.enabled = enabled
        scheme.save()
        
        serializer = self.get_serializer(scheme)
        return Response(serializer.data)