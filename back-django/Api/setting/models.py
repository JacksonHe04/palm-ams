from django.db import models

class University(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='院校名称')
    level = models.CharField(max_length=20, verbose_name='等级')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '院校等级'
        verbose_name_plural = '院校等级'

class Major(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='专业名称')
    category = models.CharField(max_length=20, verbose_name='分类')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '专业分类'
        verbose_name_plural = '专业分类'

class Personnel(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    recruitment_type = models.CharField(max_length=50, verbose_name='招生类型')
    department = models.CharField(max_length=200, verbose_name='所属院系', default='计算机学院、软件学院、东蒙联合研究生院')
    research_direction = models.CharField(max_length=200, verbose_name='研究方向', default='待定')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '人员身份'
        verbose_name_plural = '人员身份'

class AdmissionPeriod(models.Model):
    start_date = models.DateField(verbose_name='开始日期')
    end_date = models.DateField(verbose_name='结束日期')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '招生时间'
        verbose_name_plural = '招生时间'

class Award(models.Model):
    name = models.CharField(max_length=100, verbose_name='奖项名称')
    level = models.CharField(max_length=50, verbose_name='奖项等级')
    category = models.CharField(max_length=50, verbose_name='奖项类别')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '奖项信息'
        verbose_name_plural = '奖项信息'

class Year(models.Model):
    year = models.IntegerField(verbose_name='年份')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '年份信息'
        verbose_name_plural = '年份信息'