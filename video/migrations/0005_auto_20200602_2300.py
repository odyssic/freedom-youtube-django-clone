# Generated by Django 3.0.6 on 2020-06-02 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20200527_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='video',
            name='path',
            field=models.CharField(max_length=100),
        ),
    ]