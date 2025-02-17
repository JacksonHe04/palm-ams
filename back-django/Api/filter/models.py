from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
import json

class FilterScheme(models.Model):
    name = models.CharField(max_length=100, verbose_name='方案名称')
    enabled = models.BooleanField(default=True, verbose_name='是否启用')
    conditions = models.TextField(verbose_name='筛选条件')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def set_conditions(self, conditions):
        self.conditions = json.dumps(conditions, cls=DjangoJSONEncoder)

    def get_conditions(self):
        return json.loads(self.conditions) if self.conditions else []

    class Meta:
        db_table = 'filter_scheme'
        verbose_name = '筛选方案'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name