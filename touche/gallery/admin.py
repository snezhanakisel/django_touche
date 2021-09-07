from django.contrib import admin
from .models import *
# Register your models here.


class CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat')
    search_fields = ('title', )


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Gallery, GalleryAdmin)