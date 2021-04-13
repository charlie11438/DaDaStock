# Generated by Django 3.1.2 on 2021-03-20 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, verbose_name='用戶名稱')),
                ('password', models.CharField(max_length=255, verbose_name='用戶密碼')),
                ('email', models.CharField(max_length=255, verbose_name='用戶E-mail')),
                ('phone', models.CharField(max_length=255, verbose_name='用戶電話')),
                ('address', models.TextField(verbose_name='地址')),
                ('secretClientId', models.CharField(max_length=255, verbose_name='clientId')),
                ('secretToken', models.CharField(max_length=255, verbose_name='clientToken')),
                ('balance', models.IntegerField(verbose_name='餘額')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
