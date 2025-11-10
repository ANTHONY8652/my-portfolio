# Deployment Guide for Portfolio Website

## Production Readiness Checklist ✅

### ✅ Completed
- [x] Security settings configured
- [x] ALLOWED_HOSTS configured for domain support
- [x] WhiteNoise middleware added for static files
- [x] CSRF protection enabled
- [x] Media files configuration added
- [x] Contact form with CSRF token
- [x] Requirements.txt created
- [x] Environment variables setup

## Using Namecheap Domain

**YES, you can absolutely use your Namecheap domain!** Here's how:

### Step 1: Configure Domain in Namecheap

1. Log into your Namecheap account
2. Go to Domain List → Manage your domain
3. Go to Advanced DNS
4. Add/Edit A Record:
   - Type: A Record
   - Host: @
   - Value: Your server IP address
   - TTL: Automatic
5. Add/Edit A Record for www:
   - Type: A Record
   - Host: www
   - Value: Your server IP address
   - TTL: Automatic

### Step 2: Update Environment Variables

Create a `.env` file on your production server:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
NAME=your_db_name
USER=your_db_user
PASSWORD=your_db_password
HOST=localhost
PORT=5432

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com

# SSL (if using HTTPS)
SECURE_SSL_REDIRECT=True
```

### Step 3: Deployment Options

#### Option A: Deploy to Heroku
1. Install Heroku CLI
2. `heroku create your-app-name`
3. `heroku config:set ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com`
4. `git push heroku main`
5. Point Namecheap domain to Heroku (use CNAME for www, A record for root)

#### Option B: Deploy to DigitalOcean/Railway/Render
1. Create a new app/project
2. Connect your GitHub repository
3. Set environment variables
4. Deploy
5. Point Namecheap domain to your server IP

#### Option C: Deploy to VPS (Ubuntu/Debian)
1. Set up server (Ubuntu 20.04+)
2. Install Python, PostgreSQL, Nginx
3. Clone repository
4. Set up virtual environment
5. Install dependencies: `pip install -r requirements.txt`
6. Run migrations: `python manage.py migrate`
7. Collect static files: `python manage.py collectstatic --noinput`
8. Set up Gunicorn service
9. Configure Nginx as reverse proxy
10. Set up SSL with Let's Encrypt

### Step 4: Pre-Deployment Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser (for admin)
python manage.py createsuperuser
```

### Step 5: Security Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Use strong `SECRET_KEY` (generate new one)
- [ ] Set `ALLOWED_HOSTS` to your domain
- [ ] Enable HTTPS/SSL
- [ ] Set up proper database backups
- [ ] Configure email settings
- [ ] Set up monitoring/logging

### Step 6: Testing After Deployment

1. Visit your domain: `https://yourdomain.com`
2. Test all pages load correctly
3. Test contact form submission
4. Test CV download
5. Test dark mode toggle
6. Test on mobile devices
7. Check browser console for errors

## Common Issues & Solutions

### Issue: Static files not loading
**Solution:** Run `python manage.py collectstatic --noinput` and ensure WhiteNoise is configured

### Issue: 500 Error
**Solution:** Check server logs, ensure DEBUG=False and check ALLOWED_HOSTS

### Issue: CSRF errors
**Solution:** Ensure CSRF token is in forms and CSRF_COOKIE_SECURE is set correctly for HTTPS

### Issue: Database connection errors
**Solution:** Verify database credentials in .env file and ensure database is accessible

## Post-Deployment

1. Set up automated backups
2. Configure monitoring (Sentry, etc.)
3. Set up SSL certificate (Let's Encrypt)
4. Configure CDN if needed (Cloudflare)
5. Set up analytics (Google Analytics)

## Support

For issues, check:
- Django logs: `tail -f /var/log/django/error.log`
- Nginx logs: `tail -f /var/log/nginx/error.log`
- Server logs: Check your hosting provider's dashboard

