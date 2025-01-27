# Generated by Django 5.1.3 on 2024-11-13 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='personal_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='education', to='cv.personalinfo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='personal_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='cv.personalinfo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workexperience',
            name='personal_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='work_experiences', to='cv.personalinfo'),
            preserve_default=False,
        ),
    ]
