# Generated by Django 3.2.9 on 2022-04-25 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_auto_20220425_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='carrier_1',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='vote',
            name='carrier_2',
            field=models.CharField(max_length=300),
        ),
    ]
