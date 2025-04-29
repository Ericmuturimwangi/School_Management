from django.contrib import admin
from .models import SchoolClass, Attendance, Result

admin.site.register(SchoolClass)
admin.site.register(Attendance)


@admin.register(Result)
class ResultAdmin (admin.ModelAdmin):
    list_display =(
        'student',
        'school_class',
        'subject',
        'remarks',
        'date_recorded'
    )
    list_filter = ('school_class', 'subject', 'date_recorded')
    search_fields = ('student__service_number', 'subject', 'school_class__name')
    ordering = ('date_recorded',)