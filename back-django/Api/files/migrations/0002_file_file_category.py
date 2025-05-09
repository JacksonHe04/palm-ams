# Generated by Django 4.2.19 on 2025-03-22 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="file_category",
            field=models.CharField(
                choices=[("proofs", "证明材料"), ("resume", "简历")],
                default="proofs",
                max_length=20,
                verbose_name="文件类别",
            ),
        ),
    ]
