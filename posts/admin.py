from django.contrib import admin
from .models import Genre, Tag, Book

admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Book)