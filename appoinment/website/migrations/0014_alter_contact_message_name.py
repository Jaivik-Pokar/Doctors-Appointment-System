# Generated by Django 4.0.4 on 2022-05-07 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_bookapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message_name',
            field=models.EmailField(max_length=254),
        ),
    ]