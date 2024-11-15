# Generated by Django 4.1.4 on 2022-12-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platformsettings', '0007_alter_systemconfig_data_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemconfig',
            name='form_item_type',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'text'), (1, 'datetime'), (2, 'date'), (3, 'textarea'), (4, 'select'), (5, 'checkbox'), (6, 'radio'), (7, 'image'), (8, 'file'), (9, 'switch'), (10, 'number'), (11, 'array'), (12, 'images'), (13, 'time'), (14, 'richtext')], default=0, help_text='表单类型', null=True, verbose_name='表单类型'),
        ),
    ]
