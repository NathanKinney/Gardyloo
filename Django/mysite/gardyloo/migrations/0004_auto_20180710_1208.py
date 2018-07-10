# Generated by Django 2.0.6 on 2018-07-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardyloo', '0003_country_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QCapital', models.TextField()),
                ('QPoliticalLeader', models.TextField()),
                ('QCurrency', models.TextField()),
                ('QSovereignty_Date', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='country',
            name='image',
            field=models.ImageField(blank=True, default='country image', null=True, upload_to='images/'),
        ),
    ]
