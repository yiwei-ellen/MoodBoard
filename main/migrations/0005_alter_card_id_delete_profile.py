# Generated by Django 4.0 on 2021-12-14 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_card_spcolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
