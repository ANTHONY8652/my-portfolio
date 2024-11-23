from django.db import models

class HomeSection(models.Model):
    greeting = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} - {self.title}'

class Developer(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    bio = models.TextField() #Short words about yourself
    profile_image = models.ImageField(upload_to='profile_images/')
    projects_completed = models.IntegerField(default=0)
    projects_underway = models.IntegerField(default=0, blank=True)
    resume = models.FileField(upload_to='resume/', null=True, blank=True)

    def __str__(self):
        return self.name

class CV(models.Model):
    bio = models.TextField() #General information
    cv = models.FileField(upload_to='cv/', null=True, blank=True)

    def __str__(self):
        return 'CV'

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    content_type = models.CharField(max_length=50)
    value = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.content_type
    
class Counter(models.Model):
    label = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.label

class Message(models.Model):
    label = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'Message from {self.name}'
# Create your models here.
