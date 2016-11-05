from django.contrib import admin
from .models import Blog, Author
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

admin.site.register(Blog)
# admin.site.register(Author, AuthorAdmin)