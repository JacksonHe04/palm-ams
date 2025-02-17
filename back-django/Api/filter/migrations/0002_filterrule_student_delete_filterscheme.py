# Generated by Django 4.2.19 on 2025-02-17 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filter", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FilterRule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("university_rules", models.JSONField(verbose_name="高校规则")),
                ("special_rules", models.JSONField(verbose_name="特殊班级规则")),
                ("major_restrictions", models.JSONField(verbose_name="专业限制")),
                ("breakthrough_conditions", models.JSONField(verbose_name="突破条件")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
            ],
            options={
                "verbose_name": "筛选规则",
                "verbose_name_plural": "筛选规则",
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="姓名")),
                ("university", models.CharField(max_length=100, verbose_name="学校")),
                (
                    "university_level",
                    models.CharField(
                        choices=[("A", "A类"), ("B", "B类"), ("C", "C类")],
                        max_length=1,
                        verbose_name="学校等级",
                    ),
                ),
                ("major", models.CharField(max_length=100, verbose_name="专业")),
                ("rank_percentage", models.FloatField(verbose_name="排名百分比")),
                (
                    "special_class",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="特殊班级"
                    ),
                ),
                ("papers", models.JSONField(default=list, verbose_name="论文")),
                ("awards", models.JSONField(default=list, verbose_name="获奖")),
            ],
            options={
                "verbose_name": "学生",
                "verbose_name_plural": "学生",
                "ordering": ["rank_percentage"],
            },
        ),
        migrations.DeleteModel(
            name="FilterScheme",
        ),
    ]
