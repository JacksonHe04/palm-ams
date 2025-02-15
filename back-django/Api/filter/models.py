from django.db import models

class FilterScheme(models.Model):
    name = models.CharField(max_length=100, verbose_name='方案名称')
    config = models.JSONField(verbose_name='过滤配置')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '过滤方案'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']

    def __str__(self):
        return self.name