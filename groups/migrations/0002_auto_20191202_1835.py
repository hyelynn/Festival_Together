# Generated by Django 2.1 on 2019-12-02 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='maxcount',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='groups',
            name='usercount',
            field=models.IntegerField(default=1),
        ),
    ]
