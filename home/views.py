from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'title': 'Home Title',
        'text': 'Home Text By Context',
    }
    
    return render(
        request, 
        'home/index.html',
        context,
    )