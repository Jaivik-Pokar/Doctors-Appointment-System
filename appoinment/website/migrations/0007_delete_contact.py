# Generated by Django 4.0.4 on 2022-05-04 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_rename_messages_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
