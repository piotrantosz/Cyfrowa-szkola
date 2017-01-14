from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated", "author"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)
