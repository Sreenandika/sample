# Generated by Django 5.0.4 on 2024-05-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('place', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
