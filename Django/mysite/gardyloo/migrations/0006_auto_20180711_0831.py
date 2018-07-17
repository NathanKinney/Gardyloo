# Generated by Django 2.0.6 on 2018-07-11 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gardyloo', '0005_auto_20180710_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gardyloo.Country')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='QCapital',
        ),
        migrations.RemoveField(
            model_name='question',
            name='QCurrency',
        ),
        migrations.RemoveField(
            model_name='question',
            name='QPoliticalLeader',
        ),
        migrations.RemoveField(
            model_name='question',
            name='QSovereignty_Date',
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='questionanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='gardyloo.Question'),
        ),
    ]