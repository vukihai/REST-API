# Generated by Django 3.0.4 on 2020-03-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200324_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='access_token',
            field=models.CharField(default='abc', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
