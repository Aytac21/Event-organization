from django.db import models

class Venue(models.Model):
    description = models.TextField()
    location = models.CharField(max_length=255)
    size = models.PositiveIntegerField()

    def __str__(self):
        return self.description
