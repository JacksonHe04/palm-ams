# Generated by Django 4.2.19 on 2025-04-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("field", "0005_field_regioninform"),
    ]

    operations = [
        migrations.AlterField(
            model_name="field",
            name="regionInForm",
            field=models.CharField(
                default="其他", max_length=50, verbose_name="在表单中的区域"
            ),
        ),
    ]
