# Generated by Django 2.1.5 on 2019-02-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_class_class_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_code',
            field=models.IntegerField(unique=True),
        ),
    ]
