# Generated by Django 4.0.6 on 2022-07-08 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_post_image_alter_portfolio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='service', to=settings.AUTH_USER_MODEL),
        ),
    ]
