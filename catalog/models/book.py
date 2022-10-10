import uuid
from datetime import date

from django.db import models
from django.urls import reverse

from .author import Author
from .genre import Genre
from .language import Language


class Book(models.Model):
    title: str = models.CharField(max_length=200, help_text="Main title of the book.")
    suptitle: str = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Suptitle of a book, leave blank if there is none.",
    )
    author: Author = models.ForeignKey(Author, on_delete=models.RESTRICT, null=True)
    summary: str = models.TextField(
        max_length=1000, help_text="Enter a brief description of the book."
    )
    isbn: str = models.CharField(
        "ISBN",
        max_length=13,
        unique=True,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
    )
    genre: Genre = models.ManyToManyField(Genre)
    language: Language = models.ForeignKey(Language, on_delete=models.RESTRICT)
    digital_availability = models.BooleanField(default=False)
    pub_date: date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["title", "-pub_date"]

    def __str__(self) -> str:
        return f"{self.title} by {self.author.__str__()}"

    def display_genre(self) -> str:
        """
        Create a string for the Genre, this is required to display Genre in admin site.
        Only create a string out of first 3 genres to keep it readable.
        """
        return ", ".join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = "Genre"

    def get_absolute_url(self):  # REVEAL TYPE
        return revers("book-detail", args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular book across whole library.",
    )
    due_back: date = models.DateField(null=True, blank=True)
    book: Book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint: str = models.CharField(max_length=200)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Book availability",
    )

    class Meta:
        ordering = ["due_back"]

    def __str__(self) -> str:
        return f"{self.id} - {self.book.title}"
