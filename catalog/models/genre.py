from django.db import models


class Genre(models.Model):
    name: str = models.CharField(
        max_length=50, help_text="Enter a book genre (e.g. Science Fiction)"
    )
    description: str = models.CharField(
        max_length=256, help_text="Enter a brief genre description."
    )

    def __str__(self) -> str:
        return self.name
