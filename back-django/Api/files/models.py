from django.db import models
from django.utils import timezone
import os

class File(models.Model):
    applicant_id = models.CharField(max_length=50, null=True, blank=True, verbose_name='申请者ID')
    name = models.CharField(max_length=255, verbose_name='文件名')
    original_name = models.CharField(max_length=255, verbose_name='原始文件名')
    file_path = models.CharField(max_length=500, verbose_name='文件路径')
    file_size = models.BigIntegerField(verbose_name='文件大小')
    file_type = models.CharField(max_length=100, verbose_name='文件类型')
    upload_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')
    uploader = models.CharField(max_length=100, null=True, blank=True, verbose_name='上传者')
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')
    is_resume = models.BooleanField(default=False, verbose_name='是否为简历文件')
    
    class Meta:
        db_table = 'files'
        verbose_name = '文件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        """重写删除方法，实现软删除"""
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """彻底删除文件记录和实际文件"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        super().delete(*args, **kwargs)