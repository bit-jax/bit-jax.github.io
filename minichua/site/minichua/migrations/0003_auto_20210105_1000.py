# Generated by Django 3.1.4 on 2021-01-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minichua', '0002_auto_20210104_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='name',
            new_name='tag',
        ),
        migrations.AlterField(
            model_name='mini',
            name='tags',
            field=models.ManyToManyField(blank=True, to='minichua.Tags'),
        ),
    ]
