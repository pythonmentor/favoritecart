from django.db import models


class Item(models.Model):
    name = models.CharField("item name", max_length=100)

    def __str__(self):
        return self.name
