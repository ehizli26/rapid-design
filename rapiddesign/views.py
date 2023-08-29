from django.shortcuts import render

def home(request):
    context = {
        "slides" : ['1', '2'],
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def project(request):
    return render(request, 'project.html')

def service(request):
    return render(request, 'service.html')
