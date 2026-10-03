from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "course", "year_level")
    search_fields = ("first_name", "last_name", "email")
