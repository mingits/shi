from django.contrib import admin

# Register your models here.

from .models import Category_1, Category_2, Title, Song

admin.site.register(Category_1)
admin.site.register(Category_2)
admin.site.register(Title)
admin.site.register(Song)