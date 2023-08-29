from django.urls import path
from .views import (
    home, 
    about,
    contact,
    project,
    service,
)

urlpatterns = [
    path('', home, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('project/', project, name='project'),
    path('service/', service, name='service'),
]
