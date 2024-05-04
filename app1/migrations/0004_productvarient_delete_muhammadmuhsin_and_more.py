# Generated by Django 5.0.4 on 2024-05-04 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_muhammadmuhsin_rename_catogory_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVarient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('actualprice', models.CharField(max_length=20)),
                ('discountprice', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='MuhammadMuhsin',
        ),
        migrations.RemoveField(
            model_name='product',
            name='and_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='productvarient',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.product'),
        ),
    ]