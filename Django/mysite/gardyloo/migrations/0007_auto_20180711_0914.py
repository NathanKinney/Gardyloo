# Generated by Django 2.0.6 on 2018-07-11 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardyloo', '0006_auto_20180711_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
