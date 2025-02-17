from django.db import models
import time
import uuid

def generate_variable_name():
    return f'var_{int(time.time())}_{uuid.uuid4().hex}'

class Field(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='字段名称')
    description = models.TextField(verbose_name='字段描述')
    type = models.CharField(max_length=50, default='string', verbose_name='字段类型')
    variableName = models.CharField(max_length=50, default='default_var', verbose_name='变量名')
    # variableName = models.CharField(max_length=100, verbose_name='变量名', default=generate_variable_name)
    
    # def save(self, *args, **kwargs):
    #     if not self.variableName:
    #         self.variableName = f'var_{int(time.time())}_{uuid.uuid4().hex[:8]}'
    #     super().save(*args, **kwargs)
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
            'type': self.type,
            'variableName': self.variableName,
            'showInTable': self.showInTable,
            'showInFilter': self.showInFilter,
            'showInApply': self.showInApply
        }