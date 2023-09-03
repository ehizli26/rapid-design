from django.shortcuts import render
from .models import Image

def home(request):
    images = Image.objects.all()
    image_urls = [image.image.url for image in images]

    context = {
        'image_urls': image_urls,
    }

    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def project(request):
    images = Image.objects.all()
    image_urls = [image.image.url for image in images]

    context = {
        'image_urls': image_urls,
    }

    return render(request, 'project.html', context)

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')


