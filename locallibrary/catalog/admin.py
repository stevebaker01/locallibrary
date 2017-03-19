from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Book)
# admin.site.regester(Book, BookAdmin)
# admin.site.register(Author)
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(BookInstance)
# admin.site.register(BookInstance, BookInstanceAdmin)
