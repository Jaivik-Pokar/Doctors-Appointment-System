# Generated by Django 4.0.4 on 2022-05-04 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('phone', models.TextField()),
                ('email', models.TextField()),
                ('address', models.TextField()),
                ('schedule', models.TextField()),
                ('experts', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
