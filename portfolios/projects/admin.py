from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models

from .models import Project


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


class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Project, ProjectAdmin)
