# Activity Management System

A simplified Django-based activity management system for students and faculty. This system allows students to submit activity records and faculty to approve or reject them.

## 🚀 Getting Started

This project is a complete Django web application with role-based access control, file uploads, and a modern Bootstrap-based UI.

## Features

- ✅ User Authentication (Student/Faculty roles)
- ✅ Student Profile Management
- ✅ Activity Submission with File Upload
- ✅ Faculty Review Panel (Approve/Reject)
- ✅ Activity Status Tracking
- ✅ Bootstrap-based Modern UI
- ✅ Responsive Design

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 4. Run Server
```bash
python manage.py runserver
```

### 5. Access the Application
Open your browser and go to: `http://127.0.0.1:8000/`

## User Roles

### Student
- Register and create profile
- Submit activities with certificates
- View activity status (Pending/Approved/Rejected)
- View approved activities report

### Faculty
- Register and login
- View all activity submissions
- Approve or reject activities
- Filter activities by status and category

## Project Structure

```
Django/
├── config/          # Django project settings
├── core/            # Main application
│   ├── models.py    # Database models
│   ├── views.py     # View functions
│   ├── forms.py     # Form classes
│   ├── urls.py      # URL patterns
│   └── templates/   # HTML templates
├── media/           # Uploaded files (certificates)
├── db.sqlite3       # SQLite database
└── manage.py        # Django management script
```

## Database Models

- **UserProfile**: Extends User with role (Student/Faculty)
- **StudentProfile**: Stores student academic details
- **Activity**: Stores activity submissions with status

## Key URLs

- `/` - Home (redirects to login or dashboard)
- `/login/` - User login
- `/register/` - User registration
- `/student/dashboard/` - Student dashboard
- `/faculty/dashboard/` - Faculty dashboard
- `/activity/create/` - Submit new activity
- `/admin/` - Django admin panel

## Technologies Used

- Django 5.2.6
- SQLite3
- Bootstrap 5.3.0
- Bootstrap Icons

## Notes

- Media files are stored in `media/certificates/` directory
- Database is SQLite (`db.sqlite3`)
- All pages require authentication except login and register
- Students must complete profile before submitting activities

## For Viva Presentation

This project demonstrates:
1. User authentication and authorization
2. Role-based access control
3. File upload functionality
4. CRUD operations
5. Status management workflow
6. Database integration
7. Modern UI with Bootstrap

## License

This project is for educational purposes.

