# Generated by Django 4.2.19 on 2025-02-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("field", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="field",
            name="type",
            field=models.CharField(
                default="string", max_length=50, verbose_name="字段类型"
            ),
        ),
    ]
