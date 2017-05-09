from django.contrib import admin
from willblog.apps.category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'views',)


admin.site.register(Category, CategoryAdmin)
