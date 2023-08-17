from django.contrib import admin
from .models import Course,Categories

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "isActive", "slug","category")
    list_display_links = ("title","slug",)
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",),}
    list_filter = ("date", "isActive", "category")
    list_editable = ("isActive",)
    search_fields = ("title", "description", "date")

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug")
    prepopulated_fields = {"slug": ("name",),}


