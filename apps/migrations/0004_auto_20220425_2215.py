# Generated by Django 3.2.9 on 2022-04-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_alter_vote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='carrier_1',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='vote',
            name='carrier_2',
            field=models.CharField(max_length=2),
        ),
    ]
