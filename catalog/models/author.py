from datetime import date

from django.db import models
from django.urls import reverse

from .nationality import Nationality


class Author(models.Model):
    first_name: str = models.CharField(max_length=100)
    middle_names: str = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Enter middle names of the author and separate them with commas, e.g. for J.R.R. Tolkien type 'Ronald, Reuel'.",
    )
    last_name: str = models.CharField(max_length=100)
    nationality: Nationality = models.ForeignKey(Nationality, on_delete=models.RESTRICT)
    date_of_birth: date = models.DateField(null=True, blank=True)
    date_of_death: date = models.DateField("Died", null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("author-detail", args=str(self.id))
