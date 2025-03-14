# Generated by Django 4.2.19 on 2025-02-17 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filter", "0003_filterscheme_delete_filterrule_delete_student"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="filterscheme",
            name="config",
        ),
        migrations.AddField(
            model_name="filterscheme",
            name="conditions",
            field=models.TextField(default="[]", verbose_name="筛选条件"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="filterscheme",
            name="enabled",
            field=models.BooleanField(default=True, verbose_name="是否启用"),
        ),
        migrations.AlterModelTable(
            name="filterscheme",
            table="filter_scheme",
        ),
    ]