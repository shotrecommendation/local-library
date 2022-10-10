from django.contrib import admin

from .models import Author, Book, BookInstance, Genre, Language, Nationality

admin.site.register(Genre)
admin.site.register(Nationality)
admin.site.register(Language)


class AuthorAdmin(admin.ModelAdmin):
    list_display: set[str] = (
        "last_name",
        "first_name",
        "date_of_birth",
        "date_of_death",
    )
    fields: list[str] = ["first_name", "last_name", ("date_of_birth", "date_of_death")]


admin.site.register(Author, AuthorAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display: set[str] = ("title", "author", "display_genre")


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display: set[str] = ("__str__", "status", "due_back")
    list_filter: set[str] = ("status", "due_back")
