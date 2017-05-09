from django.contrib import admin
from willblog.apps.collection.models import Collection


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'views', 'create_time', 'update_time', 'ispub')
    search_fields = ('title',)


admin.site.register(Collection, CollectionAdmin)
