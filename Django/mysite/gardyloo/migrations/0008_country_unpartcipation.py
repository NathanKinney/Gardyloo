# Generated by Django 2.0.6 on 2018-07-11 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardyloo', '0007_auto_20180711_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='unPartcipation',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]