# Portfolio Website - Anthony Kang'eri Githinji

A modern, responsive portfolio website showcasing backend development skills, projects, and professional experience. Built with Django and featuring a beautiful UI with dark mode support.

## 🌟 Features

### Core Features
- ✅ **Modern UI/UX** - Polished interface with smooth animations and transitions
- ✅ **Dark Mode Toggle** - User preference persists across sessions
- ✅ **Responsive Design** - Fully optimized for all devices (mobile, tablet, desktop)
- ✅ **Contact Form** - AJAX-powered contact form with CSRF protection
- ✅ **CV Download** - Secure PDF download functionality
- ✅ **Project Showcase** - Featured Library Management API project
- ✅ **Skills Display** - Interactive progress bars for technical skills
- ✅ **Experience Timeline** - Visual timeline of work experience
- ✅ **Education Section** - Accordion-style education history
- ✅ **Social Links** - Integration with GitHub, LinkedIn, Instagram

### Technical Highlights
- **Django REST Framework** - Backend API development
- **PostgreSQL Database** - Robust data management
- **WhiteNoise** - Efficient static file serving
- **Security First** - CSRF protection, secure headers, SSL ready
- **Production Ready** - Configured for deployment with Namecheap domains

## 🛠️ Tech Stack

### Backend
- **Django 5.0.7** - Python web framework
- **Django REST Framework** - API development
- **PostgreSQL** - Database
- **WhiteNoise** - Static file serving
- **Gunicorn** - WSGI HTTP server

### Frontend
- **Bootstrap 5.3.0** - CSS framework
- **jQuery** - JavaScript library
- **Custom CSS** - Modern animations and transitions
- **Responsive Design** - Mobile-first approach

### Tools & Libraries
- **python-dotenv** - Environment variable management
- **Pillow** - Image processing

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)
- Git

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ANTHONY8652/my-portfolio.git
cd my-portfolio
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Setup

Create a `.env` file in the root directory:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
NAME=your_database_name
USER=your_database_user
PASSWORD=your_database_password
HOST=localhost
PORT=5432

# Email Configuration (Optional)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

### 5. Database Setup

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser
```

### 6. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 📁 Project Structure

```
my-portfolio/
├── my_portfolio/          # Main application
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── urls.py           # URL routing
│   ├── forms.py          # Form definitions
│   ├── admin.py          # Admin configuration
│   └── migrations/        # Database migrations
├── portfolio/            # Project settings
│   ├── settings.py       # Django settings
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI configuration
├── templates/            # HTML templates
│   └── portfolio/
│       └── index.html    # Main template
├── static/               # Static files (CSS, JS, images)
│   └── portfolio/
├── media/                # User uploaded files
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not in repo)
└── manage.py            # Django management script
```

## 🎨 Features Overview

### Home Section
- Hero slider with introduction
- Call-to-action buttons
- CV download link

### About Section
- Personal introduction
- Service cards with hover effects
- Featured achievement highlight

### Services Section
- Areas of expertise
- Interactive service cards
- Professional descriptions

### Skills Section
- Animated progress bars
- Technical proficiency display
- Skill descriptions

### Education Section
- Accordion-style education history
- Detailed program descriptions
- Professional certifications

### Experience Section
- Timeline visualization
- Work history
- Role descriptions

### Projects Section
- Featured Library Management API
- Project showcase with images
- GitHub links
- Project descriptions

### Contact Section
- Contact form with validation
- Contact information display
- Social media links

## 🔧 Configuration

### Admin Panel

Access the admin panel at `/admin/` using your superuser credentials.

### Adding Content

1. **Home Section**: Add content via Django admin → HomeSection
2. **Services**: Add via Django admin → Service
3. **Skills**: Add via Django admin → Skill
4. **Projects**: Add via Django admin → Project
5. **Contact Info**: Add via Django admin → ContactInfo

### Customization

- **Colors**: Edit CSS in `templates/portfolio/index.html` (style section)
- **Images**: Replace images in `static/portfolio/images/`
- **Content**: Update text directly in `templates/portfolio/index.html`

## 🚀 Deployment

This project is production-ready and can be deployed to various platforms:

- **Heroku** - Easy deployment with Git
- **Railway** - Modern deployment platform
- **Render** - Simple cloud hosting
- **DigitalOcean** - VPS hosting
- **AWS/GCP/Azure** - Cloud platforms

### Quick Deployment Steps

1. Set environment variables on your hosting platform
2. Set `DEBUG=False` in production
3. Configure `ALLOWED_HOSTS` with your domain
4. Run migrations: `python manage.py migrate`
5. Collect static files: `python manage.py collectstatic --noinput`
6. Deploy!

For detailed deployment instructions, see the deployment documentation (not included in repository for security).

## 🔒 Security

- ✅ CSRF protection enabled
- ✅ Secure headers configured
- ✅ Environment variables for sensitive data
- ✅ SQL injection protection (Django ORM)
- ✅ XSS protection
- ✅ SSL/HTTPS ready

## 📱 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🤝 Contributing

This is a personal portfolio project. However, suggestions and feedback are welcome!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Anthony Kang'eri Githinji**

- GitHub: [@ANTHONY8652](https://github.com/ANTHONY8652)
- LinkedIn: [Anthony Githinji](https://www.linkedin.com/in/anthony-githinji-33495422b/)
- Email: githinjianthony720@gmail.com
- Location: Nairobi, Kenya

## 🙏 Acknowledgments

- Template inspiration from Colorlib
- Icons from Icomoon
- Images from Pexels (free stock photos)
- Fonts from Google Fonts

## 📊 Project Status

✅ **Production Ready** - Fully functional and deployed-ready

## 🎯 Future Enhancements

- [ ] Blog section
- [ ] Project filtering by technology
- [ ] Multi-language support
- [ ] Analytics integration
- [ ] Performance optimizations

---

**Built with ❤️ by Anthony Githinji**

For questions or inquiries, please reach out via the contact form on the website or email directly.

