from django.shortcuts import render

def index(request):
    context = {
        'judul':'PK Reminder Cab Langsa',
        'credit':'By Muhammad Syafii'
    }
    return render(request, 'index.html', context)