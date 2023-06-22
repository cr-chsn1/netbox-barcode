# Generated by Django 4.1.8 on 2023-06-05 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0167_module_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarcodeStockDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('barcode', models.ImageField(blank=True, unique=True, upload_to='image-attachments/barcodes/')),
                ('stock_number', models.CharField(blank=True, max_length=30, null=True)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='barcode_stock', to='dcim.device')),
            ],
            options={
                'verbose_name': 'Stock Number Barcode',
                'verbose_name_plural': 'Stock Number Barcodes',
            },
        ),
        migrations.CreateModel(
            name='BarcodeSnDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('barcode', models.ImageField(blank=True, unique=True, upload_to='image-attachments/barcodes/')),
                ('sn', models.CharField(blank=True, max_length=30, null=True)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='barcode_sn', to='dcim.device')),
            ],
            options={
                'verbose_name': 'Serial Number Barcode',
                'verbose_name_plural': 'Serial Number Barcodes',
            },
        ),
        migrations.CreateModel(
            name='BarcodePartNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('barcode', models.ImageField(blank=True, unique=True, upload_to='image-attachments/barcodes/')),
                ('part_number', models.CharField(blank=True, max_length=30, null=True)),
                ('device_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='barcode_pn', to='dcim.devicetype')),
            ],
            options={
                'verbose_name': 'Part Number Barcode',
                'verbose_name_plural': 'Part Numbers Barcodes',
            },
        ),
    ]
