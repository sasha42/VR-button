from __future__ import unicode_literals
import uuid

from django.db import models

class Button(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    image = models.FileField(upload_to='')

    def __str__(self):
        return self.url