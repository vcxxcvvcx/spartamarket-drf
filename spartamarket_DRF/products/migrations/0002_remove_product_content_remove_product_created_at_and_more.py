# Generated by Django 4.2 on 2024-04-30 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='content',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('F', 'Fruit'), ('V', 'Vegetable'), ('M', 'Meat'), ('O', 'Other')], default='O', max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]