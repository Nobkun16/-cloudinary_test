from django.db import models

# Create your models here.
from cloudinary_storage.storage import MediaCloudinaryStorage

class IMG(models.Model):
   img = models.ImageField(storage=MediaCloudinaryStorage(), upload_to='my_images_folder/')

