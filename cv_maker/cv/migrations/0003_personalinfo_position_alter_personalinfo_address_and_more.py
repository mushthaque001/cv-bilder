# Generated by Django 5.1.3 on 2024-11-13 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_education_personal_info_skill_personal_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='position',
            field=models.CharField(default='Position not specified', max_length=100),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='personal_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experience', to='cv.personalinfo'),
        ),
    ]
