# Generated by Django 3.1.7 on 2021-03-30 22:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='duadate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('warning', 'normal'), ('primary', 'low')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
