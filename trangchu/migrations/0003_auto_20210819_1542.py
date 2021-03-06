# Generated by Django 3.2.5 on 2021-08-19 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trangchu', '0002_auto_20210819_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('discription', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='product',
            name='listid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trangchu.list'),
        ),
    ]
