from django.db import models

class FilterScheme(models.Model):
    name = models.CharField(max_length=100, verbose_name="方案名称")
    fields = models.JSONField(verbose_name="筛选字段")
    config = models.JSONField(verbose_name="筛选配置")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'filter_schemes'
        app_label = 'filter'
        verbose_name = "筛选方案"
        verbose_name_plural = verbose_name
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name