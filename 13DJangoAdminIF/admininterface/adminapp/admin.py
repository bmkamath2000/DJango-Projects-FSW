from django.contrib import admin
from .models import Book, Publisher, Author
# Register your models here.
admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publisher', 'publication_date')
    ordering = ('-publication_date',)
    search_fields = ('title',)
    pass
admin.site.register(Publisher)
admin.site.register(Author)