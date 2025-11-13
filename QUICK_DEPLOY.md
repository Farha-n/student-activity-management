# 🚀 Quick Deployment Guide

## Best Free Options (Ranked)

### 1. **PythonAnywhere** ⭐ EASIEST
- **URL**: https://www.pythonanywhere.com
- **Free**: ✅ Yes
- **Setup Time**: 10-15 minutes
- **Best For**: Beginners, quick deployment

**Steps**:
1. Sign up at pythonanywhere.com
2. Upload your code (via Files tab or Git)
3. Setup web app in Web tab
4. Configure WSGI file
5. Done! Your site: `yourusername.pythonanywhere.com`

---

### 2. **Render** ⭐ BEST FOR PRODUCTION
- **URL**: https://render.com
- **Free**: ✅ Yes (with limitations)
- **Setup Time**: 5-10 minutes
- **Best For**: Production apps, professional projects

**Steps**:
1. Push code to GitHub
2. Sign up at render.com (with GitHub)
3. Create new Web Service
4. Connect repository
5. Add environment variables
6. Deploy! Auto-deploys on every push

**Environment Variables**:
```
SECRET_KEY=your-generated-secret-key
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com
```

---

### 3. **Railway**
- **URL**: https://railway.app
- **Free**: ✅ Yes ($5 credit/month)
- **Setup Time**: 5 minutes
- **Best For**: Modern deployments

---

## ⚡ Pre-Deployment Checklist

### Before You Deploy:

1. **Generate Secret Key**:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **Update settings.py** (Already done! ✅):
   - Uses environment variables
   - WhiteNoise configured
   - Ready for production

3. **Collect Static Files** (Already done! ✅):
   ```bash
   python manage.py collectstatic --noinput
   ```

4. **Test Locally**:
   ```bash
   python manage.py runserver
   ```

---

## 📦 What to Upload

### ✅ Upload These:
- All `.py` files
- All `.html` templates  
- `requirements.txt`
- `manage.py`
- `Procfile` (for Render/Railway)
- `runtime.txt`
- `staticfiles/` folder
- `db.sqlite3` (if keeping SQLite)
- `media/` folder (if you have uploads)

### ❌ Don't Upload:
- `__pycache__/` folders
- `.pyc` files
- `venv/` or `env/` folders
- `.git/` (unless using Git)
- `.env` files

---

## 🎯 Recommended: PythonAnywhere (Easiest)

### Step-by-Step:

1. **Create Account**: https://www.pythonanywhere.com

2. **Upload Code**:
   - Go to **Files** tab
   - Navigate to `/home/yourusername/`
   - Upload your project folder (zip and extract, or use Git)

3. **Setup Virtual Environment**:
   - Go to **Consoles** tab
   - Start a **Bash** console
   ```bash
   cd ~/your-project-name
   python3.10 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configure Settings**:
   ```bash
   nano config/settings.py
   ```
   Change:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
   SECRET_KEY = 'your-generated-secret-key'
   ```

5. **Setup Database**:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py collectstatic --noinput
   ```

6. **Configure Web App**:
   - Go to **Web** tab
   - Click **Add a new web app**
   - Choose **Manual configuration**
   - Python 3.10
   - Click **Next**

7. **Edit WSGI File**:
   - Click **WSGI configuration file** link
   - Replace with:
   ```python
   import os
   import sys

   path = '/home/yourusername/your-project-name'
   if path not in sys.path:
       sys.path.insert(0, path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

8. **Configure Static Files**:
   - In **Web** tab → **Static files**
   - URL: `/static/`
   - Directory: `/home/yourusername/your-project-name/staticfiles`

9. **Reload**:
   - Click **Reload** button
   - Visit: `https://yourusername.pythonanywhere.com`

---

## 🎯 Alternative: Render (Best for Production)

### Step-by-Step:

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Ready for deployment"
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

2. **Create Render Account**:
   - Go to https://render.com
   - Sign up with GitHub

3. **Create Web Service**:
   - Click **New +** → **Web Service**
   - Connect your repository
   - Settings:
     - **Name**: activity-management
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
     - **Start Command**: `gunicorn config.wsgi:application`
     - **Plan**: Free

4. **Add Environment Variables**:
   ```
   SECRET_KEY=your-generated-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-app.onrender.com
   ```

5. **Deploy**:
   - Click **Create Web Service**
   - Wait for deployment (2-3 minutes)
   - Your site: `https://your-app.onrender.com`

---

## ✅ Post-Deployment

1. **Create Admin User**:
   ```bash
   python manage.py createsuperuser
   ```

2. **Test Your Site**:
   - Visit your URL
   - Test login/logout
   - Test file uploads
   - Check all pages

3. **Monitor Logs**:
   - Check platform logs for errors
   - Fix any issues

---

## 🆘 Common Issues

### Static Files Not Loading?
- Run `collectstatic` again
- Check static files configuration

### 500 Errors?
- Check `ALLOWED_HOSTS` includes your domain
- Check `DEBUG = False`
- Check server logs

### Database Errors?
- Run `python manage.py migrate`
- Check database connection

---

## 📞 Need Help?

See full guide in `DEPLOYMENT_GUIDE.md`

**Recommended**: Start with **PythonAnywhere** - it's the easiest!

