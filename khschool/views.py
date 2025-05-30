from django.shortcuts import render
from django.http import HttpResponse
from .models import Celebration
# Create your views here.
def home(request):
    return render(request,'home.html')

#gallery page
def gallery(request):
    # Get all celebrations with their related photos
    celebrations = Celebration.objects.all().order_by('-date')
    
    # Prepare celebrations with their photos for the template
    celebration_data = []
    for celebration in celebrations:
        photos = celebration.celebrationphoto_set.all().order_by('order')
        celebration_data.append({
            'celebration': celebration,
            'photos': photos,
            'photo_count': photos.count()
        })
    
    context = {
        'celebration_data': celebration_data
    }
    
    return render(request, 'gallery_new.html', context)

#contact page
def contact(request):
    return render(request,'contact.html')

#Director-brief
def brief(request):
    return render(request,'brief.html')

#school-history
def aboutSchool(request):
    return render(request,'aboutSchool.html')

#memnagar campus page
def chandkheda(request):
    return render(request,'chandkheda.html')

def chattral(request):
    return render(request,'chattral.html')

def iffco(request):
    return render(request,'iffco.html')

def kadi(request):
    return render(request,'kadi.html')
