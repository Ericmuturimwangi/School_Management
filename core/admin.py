from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import User, StudentProfile, InstructorProfile


class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'service_number', 'rank', 'role', 'is_staff')
    list_filter = ('role', 'rank', 'is_staff', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('service_number', 'rank', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'service_number', 'rank', 'role', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'service_number', 'rank')
    ordering = ('id',)


admin.site.register(User, UserAdmin)
admin.site.register(StudentProfile)
admin.site.register(InstructorProfile)