# Generated by Django 4.2.2 on 2023-07-13 09:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_orderrestaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='ID')),
                ('token', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(max_length=150)),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.restaurant')),
            ],
        ),
        migrations.DeleteModel(
            name='OrderRestaurant',
        ),
    ]
