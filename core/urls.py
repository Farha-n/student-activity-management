from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Authentication
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    
    # Student Views
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/profile/create/', views.student_profile_create, name='student_profile_create'),
    path('student/profile/edit/', views.student_profile_edit, name='student_profile_edit'),
    path('student/activities/', views.student_activities_report, name='student_activities_report'),
    
    # Activity Views
    path('activity/create/', views.activity_create, name='activity_create'),
    path('activity/<int:pk>/', views.activity_detail, name='activity_detail'),
    
    # Faculty Views
    path('faculty/dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('activity/<int:pk>/review/', views.activity_review, name='activity_review'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)