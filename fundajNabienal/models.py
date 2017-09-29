from django.db import models

# Create your models here.

class Event(models.Model):

    def __str__(self):
        return self.title
