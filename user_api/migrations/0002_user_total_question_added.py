# Generated by Django 4.1 on 2022-08-26 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='total_question_added',
            field=models.IntegerField(default=0),
        ),
    ]