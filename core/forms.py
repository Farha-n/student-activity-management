from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile, StudentProfile, Activity


# User Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'})
    )
    role = forms.ChoiceField(
        choices=UserProfile.ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='I am a'
    )
    phone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number (optional)'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role', 'phone')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a username'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})


# Login Form (Customized)
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )


# Student Profile Form
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['department', 'year', 'enrollment_number']
        widgets = {
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Computer Science'}),
            'year': forms.Select(attrs={'class': 'form-select'}),
            'enrollment_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter enrollment number (optional)'}),
        }
        labels = {
            'department': 'Department',
            'year': 'Year',
            'enrollment_number': 'Enrollment Number',
        }


# Activity Submission Form
class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['event_name', 'category', 'activity_date', 'description', 'certificate']
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event name'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'activity_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter activity description (optional)'}),
            'certificate': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*,.pdf'}),
        }
        labels = {
            'event_name': 'Event Name',
            'category': 'Category',
            'activity_date': 'Activity Date',
            'description': 'Description',
            'certificate': 'Certificate (PDF or Image)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['certificate'].required = False
        self.fields['description'].required = False


# Activity Review Form (for Faculty)
class ActivityReviewForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['status', 'rejection_reason']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'rejection_reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter reason for rejection (required if rejecting)'}),
        }
        labels = {
            'status': 'Decision',
            'rejection_reason': 'Rejection Reason',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make rejection_reason not required by default
        self.fields['rejection_reason'].required = False

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        rejection_reason = cleaned_data.get('rejection_reason', '').strip()
        
        if status == 'rejected' and not rejection_reason:
            raise forms.ValidationError({
                'rejection_reason': 'Rejection reason is required when rejecting an activity.'
            })
        
        return cleaned_data