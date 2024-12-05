# ApplicationSystem/testdb.py
"""
前人编写的测试数据库的文件，暂时不用管
"""
from django.http import HttpResponse
from Apply.models import PalmApplicant


# 数据库操作
def testdb(request):
    test1 = PalmApplicant(name_input='金虹希', grade_input=1, sex_input='F', gradepeople_input=120)
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
