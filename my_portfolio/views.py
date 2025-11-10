from django.shortcuts import render
from .models import HomeSection, Developer, CV, Service, Skill, ContactInfo, Counter, Project
from .forms import ContactForm
from django.core.mail import send_mail, EmailMessage
from portfolio.settings import EMAIL_HOST_USER
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

def index(request):
    #Fetch data from models for each section

    #Home section (greeting, name, title)
    home = HomeSection.objects.first()

    #Developer section (developer details)
    developer = Developer.objects.first()

    #CV section (bio and Resume)
    cv = CV.objects.first()

    #Services section (list of services offered)
    services = Service.objects.all()

    #skills section (skills and other profeciency)
    skills = Skill.objects.all()

    #Fetch all COntact info  from db section (contact details about anthony githinji, email, phone etc)
    contact_info = ContactInfo.objects.all()

    #Project section (portforio brojects)
    projects = Project.objects.all()

    #Counter section (stats like completed_project, years of experience, project currently underway or being undertaken currently bi I)
    counters = Counter.objects.all()

    #Context to be passed to the template
    context = {
        'home': home,
        'developer': developer,
        'cv': cv,
        'services': services,
        'skills': skills,
        'projects': projects,
        'contact_info': contact_info,
        'counters': counters,
    }
    
    # Render the 'index.html' template with the above context.
    return render(request, 'portfolio/index.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f'Message from {name} ({email}):\n\n{message}'
            send_mail(
                subject,
                full_message,
        
        'githinjianthony720@gmail.com',
        ['githinjianthony720@gmail.com'],
            )

            return JsonResponse({'success': 'Your message has been sent successfully.'}, status=status.HTTP_200_OK)

        else:
            return JsonResponse({'error': 'All fields must be filled out.'}, status=status.HTTP_400_BAD_REQUEST)
        
    return JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)

def download_cv(request):
    """View to serve the CV PDF file"""
    cv = CV.objects.first()
    if cv and cv.cv:
        try:
            return FileResponse(cv.cv.open(), as_attachment=True, filename='Anthony_Githinji_CV.pdf')
        except:
            pass
    
    # Fallback to static file if CV model doesn't have file
    static_path = os.path.join(settings.STATICFILES_DIRS[0], 'portfolio', 'resume', 'My CV.pdf')
    if os.path.exists(static_path):
        return FileResponse(open(static_path, 'rb'), as_attachment=True, filename='Anthony_Githinji_CV.pdf')
    
    raise Http404("CV not found")


# Create your views here.
