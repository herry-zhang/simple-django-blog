from django.contrib import admin
from collection.models import Collection, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views',)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'date_time')


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
