# Generated by Django 4.0.8 on 2022-11-17 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_accounttype_link_to_binary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to=images.models.image_file_path)),
                ('thumbnail_size1', models.ImageField(blank=True, null=True, upload_to=images.models.thumb_file_path)),
                ('thumbnail_size2', models.ImageField(blank=True, null=True, upload_to=images.models.thumb_file_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
