from django.db import models

class Interview(models.Model):
    student = models.CharField(max_length=100, verbose_name='学生姓名')
    score_teacher1 = models.FloatField(verbose_name='老师一打分')
    score_teacher2 = models.FloatField(verbose_name='老师二打分')
    score_teacher3 = models.FloatField(verbose_name='老师三打分')
    normalized_score = models.FloatField(null=True, blank=True, verbose_name='归一化打分')
    resume_score = models.FloatField(default=0, verbose_name='简历分数')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '面试评分'
        verbose_name_plural = verbose_name
        ordering = ['-normalized_score']

    def __str__(self):
        return f'{self.student} - {self.normalized_score}'