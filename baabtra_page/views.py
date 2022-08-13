from django.shortcuts import render

# Create your views here.


def baabtra_css(request):
    return render(request, 'baabtra_page.html')

def courses(request):
    return render(request, 'courses.html')

def contactus (request):
    return render (request, 'contactus.html')
