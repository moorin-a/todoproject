# Generated by Django 3.1.7 on 2021-03-30 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210330_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='duadate',
            field=models.DateField(),
        ),
    ]
