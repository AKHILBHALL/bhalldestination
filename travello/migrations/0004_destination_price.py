# Generated by Django 3.0.2 on 2020-01-17 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_remove_destination_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
