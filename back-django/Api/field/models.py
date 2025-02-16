from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='字段名称')
    description = models.TextField(verbose_name='字段描述')
    showInTable = models.BooleanField(default=True, verbose_name='在表格中显示')
    showInFilter = models.BooleanField(default=True, verbose_name='在筛选中显示')
    showInApply = models.BooleanField(default=True, verbose_name='在申请中显示')

    class Meta:
        db_table = 'field'
        verbose_name = '字段'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'showInTable': self.showInTable,
            'showInFilter': self.showInFilter,
            'showInApply': self.showInApply
        }