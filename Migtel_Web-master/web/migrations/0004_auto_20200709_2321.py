# Generated by Django 2.1.5 on 2020-07-10 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200707_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='cobertura',
            name='sector',
            field=models.CharField(default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='cobertura',
            name='zona',
            field=models.CharField(choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4']], max_length=20),
        ),
    ]
