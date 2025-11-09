# GitHub Setup Instructions

## ✅ Git Repository Initialized

Your project has been initialized as a Git repository and the initial commit has been created.

## 📋 Steps to Upload to GitHub

### Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and log in
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the repository details:
   - **Repository name**: `activity-management-system` (or any name you prefer)
   - **Description**: "Django-based activity management system for students and faculty"
   - **Visibility**: Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click **"Create repository"**

### Step 2: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these commands:

```bash
# Add the remote repository (replace YOUR_USERNAME and REPOSITORY_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Alternative: Using SSH (if you have SSH keys set up)

```bash
git remote add origin git@github.com:YOUR_USERNAME/REPOSITORY_NAME.git
git branch -M main
git push -u origin main
```

## 🔐 Authentication

If you're prompted for credentials:

1. **Personal Access Token** (recommended):
   - Go to GitHub Settings > Developer settings > Personal access tokens
   - Generate a new token with `repo` permissions
   - Use the token as your password when prompted

2. **GitHub CLI** (alternative):
   ```bash
   gh auth login
   ```

## 📝 Example Commands

```bash
# Navigate to your project directory
cd F:\Django

# Add remote repository (replace with your actual repository URL)
git remote add origin https://github.com/yourusername/activity-management-system.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

## ✅ Verification

After pushing, you should see all your files on GitHub. You can verify by:
1. Visiting your repository on GitHub
2. Checking that all files are present
3. Verifying that `db.sqlite3` and `media/` are NOT in the repository (they're in .gitignore)

## 🔄 Future Updates

To push future changes:

```bash
# Add changes
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push
```

## 📌 Important Notes

1. **Database**: The `db.sqlite3` file is excluded from Git (in .gitignore)
2. **Media Files**: The `media/` directory is excluded from Git
3. **Secret Key**: Make sure your `SECRET_KEY` in `settings.py` is not exposed in production
4. **Environment Variables**: Consider using environment variables for sensitive data

## 🛠️ Repository Settings (Optional)

After uploading, you can:
1. Add a repository description
2. Add topics (django, python, web-app, etc.)
3. Set up GitHub Actions for CI/CD
4. Enable GitHub Pages (if needed)
5. Add collaborators

## 📚 Additional Resources

- [GitHub Docs](https://docs.github.com/)
- [Git Documentation](https://git-scm.com/doc)
- [Django Deployment Guide](https://docs.djangoproject.com/en/stable/howto/deployment/)

---

**Status**: ✅ Git repository initialized and ready to push
**Next Step**: Create GitHub repository and push using the commands above

