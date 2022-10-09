from django.db import models


class Nationality(models.Model):
    name: str = models.CharField(max_length=50)

    def __str__(self):
        return self.name
