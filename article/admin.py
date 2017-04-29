from django.contrib import admin
from article.models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'pub_time', 'update_time')
    search_fields = ('title',)

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.author = request.user.username
        obj.save()


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
