from django.contrib import admin
from .models import Course,Categories

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "isActive", "slug",)
    list_display_links = ("title","slug",)
    readonly_fields = ("slug",)
    list_filter = ("date", "isActive")
    list_editable = ("isActive",)
    search_fields = ("title", "description", "date")

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    pass

