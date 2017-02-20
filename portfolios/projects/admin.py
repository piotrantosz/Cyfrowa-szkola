from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Project, User


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated", "author"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]

    class Meta:
        model = Project


class CustomUserAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name", "short_description", "long_description", "future_job"]
    list_editable = ["first_name", "last_name", "short_description", "long_description", "future_job"]

    class Meta:
        model = User


admin.site.register(User, CustomUserAdmin)
admin.site.register(Project, ProjectAdmin)
