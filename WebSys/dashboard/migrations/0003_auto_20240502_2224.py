# Generated by Django 5.0.4 on 2024-05-02 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_product_category_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name="order",
        )
        
    ]