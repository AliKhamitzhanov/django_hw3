from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=20, unique=True)
    logo = models.ImageField(upload_to='Brand_logo', null=True, blank=True)

    def __str__(self):
        return self.name
