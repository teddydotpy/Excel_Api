# Generated by Django 3.1.5 on 2021-06-23 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='U_ContactNo',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
    ]
