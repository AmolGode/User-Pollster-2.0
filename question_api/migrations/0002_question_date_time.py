# Generated by Django 4.0.7 on 2022-08-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
