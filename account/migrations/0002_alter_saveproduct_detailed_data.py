# Generated by Django 4.2.2 on 2023-07-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveproduct',
            name='detailed_data',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
    ]