from django.contrib import admin
from .models import CategorieDish,Dish

# Register your models here.
class DishAdmin(admin.ModelAdmin):
    list_display = ('name','cat', 'price')
    search_fields = ('name', 'price',)

admin.site.register(CategorieDish)
admin.site.register(Dish, DishAdmin)
