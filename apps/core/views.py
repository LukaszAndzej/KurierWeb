from django.shortcuts import render

def home_view(request):
    """
    Główna strona (landing page).
    """
    return render(request, 'core/home.html')
