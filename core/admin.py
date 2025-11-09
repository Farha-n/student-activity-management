from django.contrib import admin
from .models import UserProfile, StudentProfile, Activity


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone')
    raw_id_fields = ('user',)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'department', 'year', 'enrollment_number', 'created_at')
    list_filter = ('department', 'year', 'created_at')
    search_fields = ('user_profile__user__username', 'department', 'enrollment_number')
    raw_id_fields = ('user_profile',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'student_profile', 'category', 'activity_date', 'status', 'created_at')
    list_filter = ('category', 'status', 'activity_date', 'created_at')
    search_fields = ('event_name', 'student_profile__user_profile__user__username', 'description')
    raw_id_fields = ('student_profile', 'reviewed_by')
    date_hierarchy = 'activity_date'
