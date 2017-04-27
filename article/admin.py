from django.contrib import admin
from article.models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'date_time')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
