# Generated by Django 3.1.4 on 2021-01-15 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minichua', '0004_auto_20210106_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='mini',
            name='url',
            field=models.CharField(default='url', max_length=200),
            preserve_default=False,
        ),
    ]
