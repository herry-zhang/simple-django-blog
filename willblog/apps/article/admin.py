from django.contrib import admin
from willblog.apps.article.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'views', 'create_time', 'update_time', 'ispub')
    search_fields = ('title',)


admin.site.register(Article, ArticleAdmin)
