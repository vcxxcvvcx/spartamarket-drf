# Generated by Django 4.2 on 2024-05-01 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_content_remove_product_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
