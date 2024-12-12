from django.shortcuts import render

def learn(request):
    return render(request, 'learn.html')

def create(request):
    return render(request, 'create.html')

def stats(request):
    return render(request, 'stats.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html')

def payments(request):
    return render(request, 'payments.html')