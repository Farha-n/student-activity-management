# Activity Management System - Website Information

## 📋 What is the Use of the Website?

This is a **Django Activity Management System** designed for managing student activities with role-based access control. The system allows students to submit activity records and faculty to approve or reject them.

## 🔑 Core Features

### 1. User Authentication (Basic Role-Based Access)
- ✅ **Login System** - Students and faculty log in through the same page
- ✅ **Registration System** - Users can register as either Student or Faculty
- ✅ **Role-Based Access Control** - Different dashboards for students and faculty

### 2. Student Profile & Activity Submission
- ✅ **Student Profile** - Students fill in their personal and academic details (department, year, enrollment number)
- ✅ **Activity Submission** - Students can upload activity details (event name, category, date, and upload certificate as PDF or image)
- ✅ **Activity Categories** - Categorized into curricular, co-curricular, or extra-curricular
- ✅ **Activity Status Tracking** - View pending, approved, and rejected activities

### 3. Faculty Validation Panel
- ✅ **Activity Review** - Faculty can view all activity submissions
- ✅ **Approve/Reject** - Faculty can approve or reject submissions
- ✅ **Rejection Reason** - Rejected submissions show a reason for rejection
- ✅ **Filtering** - Faculty can filter activities by status and category

### 4. Basic Report View
- ✅ **Student Activities Report** - Students can view a list of their approved activities
- ✅ **Activity Details** - View detailed information about each activity
- ✅ **Certificate Download** - View and download uploaded certificates

### 5. Minimal UI — Simple & Clean
- ✅ **Bootstrap UI** - Uses Django's in-built template engine with Bootstrap 5 for modern UI
- ✅ **Responsive Design** - Works on desktop and mobile devices
- ✅ **User-Friendly Navigation** - Easy-to-use navigation menu

## 🚀 How to Use the Website

### Start the Server:
```bash
python manage.py runserver
```

### Available Pages:

#### Authentication Pages:
- **Home/Login:** `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/login/`
- **Register:** `http://127.0.0.1:8000/register/`

#### Student Pages:
- **Student Dashboard:** `http://127.0.0.1:8000/student/dashboard/`
- **Submit Activity:** `http://127.0.0.1:8000/activity/create/`
- **My Activities Report:** `http://127.0.0.1:8000/student/activities/`
- **Edit Profile:** `http://127.0.0.1:8000/student/profile/edit/`

#### Faculty Pages:
- **Faculty Dashboard:** `http://127.0.0.1:8000/faculty/dashboard/`
- **Review Activity:** `http://127.0.0.1:8000/activity/<id>/review/`

#### Admin Panel:
- **Django Admin:** `http://127.0.0.1:8000/admin/`

## 💾 Database Models

### UserProfile
- Extends Django's User model with role (Student/Faculty)
- Stores: user, role, phone, created_at, updated_at

### StudentProfile
- Stores student academic details
- Stores: user_profile, department, year, enrollment_number, created_at, updated_at

### Activity
- Stores activity submissions
- Stores: student_profile, event_name, category, activity_date, description, certificate, status, rejection_reason, reviewed_by, reviewed_at, created_at, updated_at

## 🔄 User Flow

### Student Flow:
1. **Register** → Create account as Student
2. **Complete Profile** → Fill in department, year, enrollment number
3. **Submit Activity** → Upload activity details and certificate
4. **View Status** → Check if activity is approved, pending, or rejected
5. **View Report** → See all approved activities

### Faculty Flow:
1. **Register** → Create account as Faculty
2. **Login** → Access faculty dashboard
3. **View Submissions** → See all activity submissions
4. **Review Activity** → Approve or reject with reason
5. **Filter Activities** → Filter by status and category

## 📊 Database Location

**Database File:** `db.sqlite3` (in the project root directory)

### Data Storage:
- **User Profiles** → `core_userprofile` table
- **Student Profiles** → `core_studentprofile` table
- **Activities** → `core_activity` table
- **Users** → `auth_user` table (Django's built-in User model)

## 🔐 Authentication System

### Login Required:
- All pages except login and register require authentication
- Users are redirected to login if not authenticated
- Role-based access control ensures students and faculty see appropriate pages

### User Roles:
- **Student** - Can submit activities, view their own activities, edit profile
- **Faculty** - Can review all activities, approve/reject submissions

## 📁 File Uploads

### Media Files:
- **Location:** `media/certificates/` directory
- **Supported Formats:** PDF and Images
- **Access:** Files are served at `/media/certificates/` URL

## 🎯 Key Features for Viva Presentation

1. **Simple yet Complete** - Easy to explain, demonstrates real functionality
2. **Role-Based Access** - Shows authentication and authorization
3. **File Upload** - Demonstrates file handling
4. **CRUD Operations** - Create, Read, Update operations for activities
5. **Status Management** - Activity approval workflow
6. **Clean UI** - Bootstrap-based modern interface
7. **Database Integration** - SQLite database with proper models

## 📌 Important Notes

1. **Registration Creates Account** - Registration now creates a login account (unlike the old system)
2. **Role Selection** - Users must select their role (Student or Faculty) during registration
3. **Student Profile Required** - Students must complete their profile before submitting activities
4. **Activity Status** - Activities start as "Pending" and can be "Approved" or "Rejected" by faculty
5. **Certificate Upload** - Certificates are optional but recommended
6. **Data Persistence** - All data is permanently saved in the SQLite database

## 🛠️ Technical Stack

- **Backend:** Django 5.2.6
- **Database:** SQLite3
- **Frontend:** Bootstrap 5.3.0
- **Icons:** Bootstrap Icons
- **Template Engine:** Django Templates

## 📝 Future Scope (Mention in Viva)

- Detailed analytics/graphs
- Multi-level admin dashboards
- Advanced notifications system
- Automated NAAC/NBA reporting
- Email notifications
- PDF report generation
- Activity search and advanced filtering

## 🔧 Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Create Superuser (Optional):**
   ```bash
   python manage.py createsuperuser
   ```

4. **Run Server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the Application:**
   - Open browser and go to `http://127.0.0.1:8000/`
   - Register as a Student or Faculty
   - Start using the system!

## ✅ Summary

| Feature | Status | Details |
|---------|--------|---------|
| User Registration | ✅ Working | Creates user account with role selection |
| User Login | ✅ Working | Authenticates users and redirects based on role |
| Student Profile | ✅ Working | Stores academic details (department, year, enrollment) |
| Activity Submission | ✅ Working | Students can submit activities with certificates |
| Faculty Review | ✅ Working | Faculty can approve/reject activities |
| Activity Reports | ✅ Working | Students can view approved activities |
| File Upload | ✅ Working | Supports PDF and image certificates |
| Role-Based Access | ✅ Working | Different dashboards for students and faculty |
| Database Storage | ✅ Working | All data saved in SQLite database |
| Bootstrap UI | ✅ Working | Modern, responsive user interface |

---

**Last Updated:** November 2024
**Version:** 2.0 (Simplified Activity Management System)
