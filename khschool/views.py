from django.shortcuts import render
from django.http import HttpResponse
from .models import Celebration, CarouselImage
# Create your views here.
def home(request):
    # Handle the case where the CarouselImage table might not exist yet
    try:
        carousel_images = CarouselImage.objects.filter(is_active=True).order_by('order')
    except Exception:
        # If there's any error (like table doesn't exist), set carousel_images to empty list
        carousel_images = []
    
    # Get celebration data for the home page
    try:
        celebrations = Celebration.objects.all().order_by('-date')[:3]
    except Exception:
        celebrations = []
        
    context = {
        'carousel_images': carousel_images,
        'celebration': celebrations
    }
    
    return render(request, 'home.html', context)

#gallery page
def gallery(request):
    # Get all celebrations with their related photos
    celebrations = Celebration.objects.all().order_by('-date')
    
    # Create a dictionary to store celebration photos
    celebration_photos = {}
    
    # For each celebration, get its additional photos
    for celebration in celebrations:
        photos = celebration.celebrationphoto_set.all().order_by('order')
        celebration_photos[celebration.id] = photos
    
    context = {
        'celebration': celebrations,
        'celebration_photos': celebration_photos
    }
    
    return render(request, 'gallery.html', context)

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
