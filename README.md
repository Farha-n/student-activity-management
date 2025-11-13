# Activity Management System

A modern Django-based activity management system for students and faculty with a beautiful dark-themed UI.

## 🚀 Quick Start

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

### 4. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 5. Run Server
```bash
python manage.py runserver
```

### 6. Access the Application
Open your browser and go to: `http://127.0.0.1:8000/`

---

## ✨ Features

- ✅ User Authentication (Student/Faculty roles)
- ✅ Student Profile Management
- ✅ Activity Submission with File Upload
- ✅ Faculty Review Panel (Approve/Reject)
- ✅ Activity Status Tracking
- ✅ Modern Dark Theme UI with Blue/Purple Gradient
- ✅ Interactive Dashboard with Charts
- ✅ Responsive Design
- ✅ Activity Reports

---

## 🎨 UI Features

- **Dark Theme**: Beautiful blue/purple gradient design
- **Interactive Dashboards**: Charts and visualizations
- **Modern Cards**: Glowing effects and smooth animations
- **Responsive**: Works on all devices

---

## 👥 User Roles

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

---

## 📁 Project Structure

```
Django/
├── config/          # Django project settings
├── core/            # Main application
│   ├── models.py    # Database models
│   ├── views.py     # View functions
│   ├── forms.py     # Form classes
│   ├── urls.py      # URL patterns
│   ├── templates/   # HTML templates
│   └── static/      # CSS, JS files
├── media/           # Uploaded files (certificates)
├── staticfiles/     # Collected static files
├── db.sqlite3       # SQLite database
└── manage.py        # Django management script
```

---

## 🌐 Deployment

### Free Hosting Options:

1. **PythonAnywhere** (Easiest) - https://www.pythonanywhere.com
2. **Render** (Best Overall) - https://render.com
3. **Railway** - https://railway.app
4. **Fly.io** - https://fly.io

**See `DEPLOYMENT_GUIDE.md` for detailed deployment instructions.**

### Quick Deployment Steps:

1. **Generate Secret Key**:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **Update Settings**:
   - Set `DEBUG = False`
   - Update `ALLOWED_HOSTS` with your domain
   - Set `SECRET_KEY` from environment variable

3. **Collect Static Files**:
   ```bash
   python manage.py collectstatic --noinput
   ```

4. **Deploy** following platform-specific instructions in `DEPLOYMENT_GUIDE.md`

---

## 🔑 Key URLs

- `/` - Home (redirects to login or dashboard)
- `/login/` - User login
- `/register/` - User registration
- `/student/dashboard/` - Student dashboard
- `/faculty/dashboard/` - Faculty dashboard
- `/activity/create/` - Submit new activity
- `/admin/` - Django admin panel

---

## 🛠️ Technologies Used

- Django 5.2.6
- SQLite3 (can switch to PostgreSQL for production)
- Bootstrap 5.3.0
- Bootstrap Icons
- Chart.js 4.4.0
- WhiteNoise (for static files in production)

---

## 📝 Notes

- Media files are stored in `media/certificates/` directory
- Database is SQLite (`db.sqlite3`) - can switch to PostgreSQL
- All pages require authentication except login and register
- Students must complete profile before submitting activities
- Static files are collected in `staticfiles/` directory

---

## 🔒 Security

For production deployment:
- Set `DEBUG = False`
- Use environment variables for `SECRET_KEY`
- Update `ALLOWED_HOSTS`
- Enable HTTPS
- Use PostgreSQL instead of SQLite for production

---

## 📄 License

This project is for educational purposes.

---

## 🆘 Support

For deployment help, see `DEPLOYMENT_GUIDE.md`

For troubleshooting, check server logs and Django documentation.
