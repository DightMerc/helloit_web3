from django.db import models

# Create your models here.
class Fruit(models.Model):
    title = models.CharField("Название", max_length=255, null=False, blank=False, default=None)
    shape = models.CharField("Форма", max_length=255, null=True, blank=True, default=None)

    def __str__(self):
        return self.title