# Generated by Django 4.1.3 on 2022-12-15 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poll', '0012_completeregistration_can_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completeregistration',
            name='can_vote',
        ),
        migrations.CreateModel(
            name='CanVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_vote', models.BooleanField(default=True)),
                ('relation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
