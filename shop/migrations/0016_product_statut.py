# Generated by Django 5.0.1 on 2024-06-01 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_product_adresse_product_nombre_piece'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='statut',
            field=models.CharField(default='A vendre', max_length=20),
        ),
    ]
