# Generated by Django 5.2 on 2025-06-23 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
