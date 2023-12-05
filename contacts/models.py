from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contacts(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=20)
    contact_picture = models.ImageField(upload_to="all_images", null=True)
    is_favorite = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name
