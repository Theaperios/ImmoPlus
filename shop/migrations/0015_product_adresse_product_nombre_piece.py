# Generated by Django 5.0.1 on 2024-05-31 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_category_description_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='adresse',
            field=models.CharField(default='Abidjan', max_length=40),
        ),
        migrations.AddField(
            model_name='product',
            name='nombre_piece',
            field=models.IntegerField(default=3),
        ),
    ]
