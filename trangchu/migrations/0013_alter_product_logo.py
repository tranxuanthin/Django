# Generated by Django 3.2.5 on 2021-08-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trangchu', '0012_alter_product_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='logo',
            field=models.ImageField(default='no_picture.png', upload_to=''),
        ),
    ]
