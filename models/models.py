from django.db import models
from brands.models import Brand
# Create your models here.


class Model(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name="Модель машины")
    engine = models.CharField(max_length=60)
    hp = models.IntegerField(null=True)
    nm = models.IntegerField(null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='model_img', null=True, blank=True)

    def __str__(self):
        return self.name


class Series(models.Model):
    name_series = models.CharField(max_length=40, unique=True)
    engine_series = models.CharField(max_length=60)
    hp_series = models.IntegerField(null=True)
    nm_series = models.IntegerField(null=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=False)
    image_series = models.ImageField(upload_to='model_series_img', null=True, blank=True)

    def __str__(self):
        return f'{self.model.name} in {self.name_series}'
