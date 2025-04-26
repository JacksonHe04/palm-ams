from django.db import models

class AdmissionDate(models.Model):
    """
    招生时间配置模型
    """
    ADMISSION_TYPES = [
        ('推免硕士', '推免硕士'),
        ('考研硕士', '考研硕士'),
        ('博士', '博士'),
        ('直博', '直博'),
    ]

    year = models.IntegerField(verbose_name='年份')
    type = models.CharField(max_length=20, choices=ADMISSION_TYPES, verbose_name='招生类型')
    start_time = models.DateTimeField(verbose_name='开始时间', null=True, blank=True)
    end_time = models.DateTimeField(verbose_name='结束时间', null=True, blank=True)

    class Meta:
        verbose_name = '招生时间配置'
        verbose_name_plural = verbose_name
        unique_together = ('year', 'type')  # 确保同一年份同一类型只有一条记录

    def __str__(self):
        return f"{self.year}年 {self.type}"