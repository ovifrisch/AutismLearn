# Generated by Django 2.1.5 on 2019-02-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190210_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]
