# Generated by Django 5.1.4 on 2024-12-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('graduationYear', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('birthDate', models.DateField()),
                ('photo', models.ImageField(upload_to='apply/')),
                ('university', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=50)),
                ('majorCount', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('percentage', models.CharField(max_length=10)),
                ('masterUniversity', models.CharField(max_length=50)),
                ('masterMajor', models.CharField(max_length=50)),
                ('tutor', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('applicationType', models.CharField(max_length=50)),
                ('firstChoice', models.CharField(max_length=50)),
                ('secondChoice', models.CharField(max_length=50)),
                ('thirdChoice', models.CharField(max_length=50)),
                ('isAdjustable', models.BooleanField()),
                ('proofs', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
