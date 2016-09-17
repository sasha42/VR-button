from __future__ import unicode_literals

from django.db import models

class Button(models.Model):
    url = models.URLField()
    image = models.FileField(upload_to='')

    def __str__(self):
        return self.url