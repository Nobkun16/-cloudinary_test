# Generated by Django 5.2 on 2025-04-26 05:35

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_img', '0002_alter_img_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='my_images_folder/'),
        ),
    ]
