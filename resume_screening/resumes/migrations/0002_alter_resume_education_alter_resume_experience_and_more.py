# Generated by Django 4.2.16 on 2025-01-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
