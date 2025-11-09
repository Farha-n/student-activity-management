from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .forms import UserRegistrationForm, UserLoginForm, StudentProfileForm, ActivityForm, ActivityReviewForm
from .models import UserProfile, StudentProfile, Activity


# Home View
def home(request):
    """Home page - shows landing page or redirects to dashboard if authenticated"""
    if request.user.is_authenticated:
        if hasattr(request.user, 'profile'):
            if request.user.profile.role == 'student':
                return redirect('student_dashboard')
            elif request.user.profile.role == 'faculty':
                return redirect('faculty_dashboard')
    return render(request, 'home.html')


# User Registration View
def register(request):
    """User registration view - creates user account and profile"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Create UserProfile
            role = form.cleaned_data.get('role')
            phone = form.cleaned_data.get('phone', '')
            user_profile = UserProfile.objects.create(
                user=user,
                role=role,
                phone=phone
            )
            
            # If student, redirect to complete profile
            if role == 'student':
                messages.success(request, 'Registration successful! Please complete your student profile.')
                login(request, user)
                return redirect('student_profile_create')
            else:
                messages.success(request, 'Registration successful! You can now login.')
                return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})


# User Login View
def user_login(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            
            # Redirect based on role
            if hasattr(user, 'profile'):
                if user.profile.role == 'student':
                    return redirect('student_dashboard')
                elif user.profile.role == 'faculty':
                    return redirect('faculty_dashboard')
            
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', {'form': form})


# User Logout View
@login_required
def user_logout(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


# Student Profile Create/Update View
@login_required
def student_profile_create(request):
    """Create or update student profile"""
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'student':
        messages.error(request, 'Access denied. This page is for students only.')
        return redirect('home')
    
    # Check if profile already exists
    try:
        student_profile = request.user.profile.student_profile
        return redirect('student_profile_edit')
    except StudentProfile.DoesNotExist:
        pass
    
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            student_profile = form.save(commit=False)
            student_profile.user_profile = request.user.profile
            student_profile.save()
            messages.success(request, 'Student profile created successfully!')
            return redirect('student_dashboard')
    else:
        form = StudentProfileForm()
    
    return render(request, 'student_profile_form.html', {'form': form, 'action': 'Create'})


@login_required
def student_profile_edit(request):
    """Edit student profile"""
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'student':
        messages.error(request, 'Access denied. This page is for students only.')
        return redirect('home')
    
    try:
        student_profile = request.user.profile.student_profile
    except StudentProfile.DoesNotExist:
        return redirect('student_profile_create')
    
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=student_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student profile updated successfully!')
            return redirect('student_dashboard')
    else:
        form = StudentProfileForm(instance=student_profile)
    
    return render(request, 'student_profile_form.html', {'form': form, 'action': 'Edit'})


# Student Dashboard View
@login_required
def student_dashboard(request):
    """Student dashboard - view activities and submit new ones"""
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'student':
        messages.error(request, 'Access denied. This page is for students only.')
        return redirect('home')
    
    # Get or create student profile
    try:
        student_profile = request.user.profile.student_profile
    except StudentProfile.DoesNotExist:
        messages.info(request, 'Please complete your student profile first.')
        return redirect('student_profile_create')
    
    # Get all activities for this student
    activities = Activity.objects.filter(student_profile=student_profile).order_by('-created_at')
    
    # Statistics
    stats = {
        'total': activities.count(),
        'approved': activities.filter(status='approved').count(),
        'pending': activities.filter(status='pending').count(),
        'rejected': activities.filter(status='rejected').count(),
    }
    
    context = {
        'student_profile': student_profile,
        'activities': activities,
        'stats': stats,
    }
    
    return render(request, 'student_dashboard.html', context)


# Activity Create View
@login_required
def activity_create(request):
    """Create a new activity submission"""
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'student':
        messages.error(request, 'Access denied. This page is for students only.')
        return redirect('home')
    
    try:
        student_profile = request.user.profile.student_profile
    except StudentProfile.DoesNotExist:
        messages.info(request, 'Please complete your student profile first.')
        return redirect('student_profile_create')
    
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.student_profile = student_profile
            activity.save()
            messages.success(request, 'Activity submitted successfully! It is now pending approval.')
            return redirect('student_dashboard')
    else:
        form = ActivityForm()
    
    return render(request, 'activity_form.html', {'form': form, 'action': 'Submit'})


# Activity Detail View
@login_required
def activity_detail(request, pk):
    """View activity details"""
    activity = get_object_or_404(Activity, pk=pk)
    
    # Check permissions
    if not hasattr(request.user, 'profile'):
        messages.error(request, 'Access denied. Please complete your profile.')
        return redirect('home')
    
    if request.user.profile.role == 'student':
        if activity.student_profile.user_profile != request.user.profile:
            messages.error(request, 'Access denied.')
            return redirect('student_dashboard')
    elif request.user.profile.role == 'faculty':
        pass  # Faculty can view all activities
    else:
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    return render(request, 'activity_detail.html', {'activity': activity})


# Faculty Dashboard View
@login_required
def faculty_dashboard(request):
    """Faculty dashboard - view and review activity submissions"""
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'faculty':
        messages.error(request, 'Access denied. This page is for faculty only.')
        return redirect('home')
    
    # Get all activities
    activities = Activity.objects.select_related('student_profile__user_profile__user').all().order_by('-created_at')
    
    # Filter options
    status_filter = request.GET.get('status', 'all')
    if status_filter != 'all':
        activities = activities.filter(status=status_filter)
    
    category_filter = request.GET.get('category', 'all')
    if category_filter != 'all':
        activities = activities.filter(category=category_filter)
    
    # Statistics
    stats = {
        'total': Activity.objects.count(),
        'pending': Activity.objects.filter(status='pending').count(),
        'approved': Activity.objects.filter(status='approved').count(),
        'rejected': Activity.objects.filter(status='rejected').count(),
    }
    
    context = {
        'activities': activities,
        'stats': stats,
        'status_filter': status_filter,
        'category_filter': category_filter,
    }
    
    return render(request, 'faculty_dashboard.html', context)


# Activity Review View
@login_required
def activity_review(request, pk):
    """Review and approve/reject activity"""
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'faculty':
        messages.error(request, 'Access denied. This page is for faculty only.')
        return redirect('home')
    
    activity = get_object_or_404(Activity, pk=pk)
    
    if request.method == 'POST':
        form = ActivityReviewForm(request.POST, instance=activity)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.reviewed_by = request.user
            activity.reviewed_at = timezone.now()
            
            # Clear rejection reason if approved
            if activity.status == 'approved':
                activity.rejection_reason = ''
            
            activity.save()
            
            status_msg = 'approved' if activity.status == 'approved' else 'rejected'
            messages.success(request, f'Activity has been {status_msg} successfully!')
            return redirect('faculty_dashboard')
    else:
        form = ActivityReviewForm(instance=activity)
    
    return render(request, 'activity_review.html', {'activity': activity, 'form': form})


# Student Activities Report View (for viewing approved activities)
@login_required
def student_activities_report(request):
    """View approved activities report"""
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'student':
        messages.error(request, 'Access denied. This page is for students only.')
        return redirect('home')
    
    try:
        student_profile = request.user.profile.student_profile
    except StudentProfile.DoesNotExist:
        messages.info(request, 'Please complete your student profile first.')
        return redirect('student_profile_create')
    
    # Get approved activities only
    activities = Activity.objects.filter(
        student_profile=student_profile,
        status='approved'
    ).order_by('-activity_date')
    
    return render(request, 'student_activities_report.html', {
        'student_profile': student_profile,
        'activities': activities,
    })
