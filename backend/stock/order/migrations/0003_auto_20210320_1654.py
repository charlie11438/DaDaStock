# Generated by Django 3.1.2 on 2021-03-20 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210309_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='takeprice',
            field=models.CharField(default='', max_length=255, verbose_name='取價類別'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='tradeCategory',
            field=models.CharField(default='', max_length=255, verbose_name='交易種類'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='tradeType',
            field=models.CharField(default='', max_length=255, verbose_name='交易類別'),
            preserve_default=False,
        ),
    ]
