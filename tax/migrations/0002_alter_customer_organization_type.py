# Generated by Django 4.2.4 on 2024-05-16 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='organization_type',
            field=models.CharField(choices=[('O', 'Others'), ('TR', 'Not Government'), ('GO', 'Government'), ('LC', 'Limited Company'), ('PJ', 'Partner / Joint Venture')], max_length=2),
        ),
    ]
