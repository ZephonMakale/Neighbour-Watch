# Generated by Django 3.1 on 2021-02-01 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourwatc', '0002_auto_20210201_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='biz_email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
