# Generated by Django 4.1.3 on 2023-01-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0021_adminsitting1_be_inform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completeregistration',
            name='profile_picture',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
