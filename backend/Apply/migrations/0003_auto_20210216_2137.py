# Generated by Django 3.1.6 on 2021-02-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0002_auto_20210216_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palmapplicant',
            name='ajustment_input',
            field=models.CharField(default='是', max_length=10, verbose_name='服从分配'),
        ),
    ]
