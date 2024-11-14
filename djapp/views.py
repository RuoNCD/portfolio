from django.shortcuts import render

def home(requests):
    return render(requests, 'home.html')

def about(requests):
    return render(requests, 'about.html')

def projects(requests):
    return render(requests, 'projects.html')

def contact(requests):
    return render(requests, 'contact.html')
