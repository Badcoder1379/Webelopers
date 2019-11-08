from django.contrib import admin

from home.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
