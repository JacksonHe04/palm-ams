from django.db import models


class TestStudent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    grade = models.CharField(max_length=20)

    class Meta:
        db_table = 'test_student'
