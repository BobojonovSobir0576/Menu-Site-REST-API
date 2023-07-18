# Generated by Django 4.2.2 on 2023-07-18 06:11

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_saveproduct_detailed_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=150, null=True)),
                ('phone', models.CharField(blank=True, max_length=150, null=True)),
                ('detailed_data', models.JSONField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='save_product')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.restaurant')),
            ],
            managers=[
                ('obj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='SaveProduct',
        ),
    ]