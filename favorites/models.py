from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Favorite(models.Model):
    item = models.ForeignKey("items.Item", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        unique_together = (('item', 'user'),)

    def __str__(self):
        return f"{self.item.name} ({self.user.username})"
