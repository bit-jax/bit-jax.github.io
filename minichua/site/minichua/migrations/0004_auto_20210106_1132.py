# Generated by Django 3.1.4 on 2021-01-06 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minichua', '0003_auto_20210105_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mini',
            name='image_url',
            field=models.CharField(max_length=600),
        ),
    ]
