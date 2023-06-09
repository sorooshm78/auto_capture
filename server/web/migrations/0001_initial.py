# Generated by Django 4.2 on 2023-04-27 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScreenShot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=web.models.get_file_upload_path)),
                ('created', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenshots', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
