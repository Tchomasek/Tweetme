# Generated by Django 2.2 on 2020-12-03 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20201203_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-id']},
        ),
    ]
