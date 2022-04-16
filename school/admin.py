from django.contrib import admin

from school.models import Student, Course, Enrollment


class StudentAdmin(admin.ModelAdmin):
    """Admin view for Studen model."""
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


class CourseAdmin(admin.ModelAdmin):
    """Admin view for Course model."""
    list_display = ('id', 'course_code', 'description')
    list_display_links = ('id', 'course_code')
    search_fields = ('course_code',)


class EnrollmentAdmin(admin.ModelAdmin):
    """Admin view for Enrollment model."""
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id',)


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
