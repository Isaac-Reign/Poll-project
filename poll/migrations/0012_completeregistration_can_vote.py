# Generated by Django 4.1.3 on 2022-12-15 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0011_remove_completeregistration_can_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='completeregistration',
            name='can_vote',
            field=models.BooleanField(default=True),
        ),
    ]
