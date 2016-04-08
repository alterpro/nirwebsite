from django.utils.timezone import now
from django.db import models

class MenuItemManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(title=name)
