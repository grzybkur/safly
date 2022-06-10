# Generated by Django 3.2.9 on 2022-04-25 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_choice', models.IntegerField()),
                ('carrier_1', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='carrier_1', to='apps.airline')),
                ('carrier_2', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='carrier_2', to='apps.airline')),
            ],
        ),
    ]