# Generated by Django 4.2.3 on 2023-10-15 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_product_status_alter_product_trending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=700),
        ),
    ]