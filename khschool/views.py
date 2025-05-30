from django.shortcuts import render
from django.http import HttpResponse
from .models import Celebration, CarouselImage
# Create your views here.
def home(request):
    # Set default empty values
    carousel_images = []
    celebrations = []
    
    # Handle the case where the CarouselImage table might not exist yet
    try:
        carousel_images = CarouselImage.objects.filter(is_active=True).order_by('order')
    except Exception as e:
        # Just continue with empty list if there's an error
        pass
    
    # Get celebration data for the home page
    try:
        celebrations = Celebration.objects.all().order_by('-date')[:3]
    except Exception as e:
        # Just continue with empty list if there's an error
        pass
        
    context = {
        'carousel_images': carousel_images,
        'celebration': celebrations
    }
    
    return render(request, 'home.html', context)

#gallery page
def gallery(request):
    # Get all celebrations with their related photos
    celebrations = Celebration.objects.all().order_by('-date')
    
    # For each celebration, get its additional photos
    for celebration in celebrations:
        # Add a photo_count attribute to each celebration object
        try:
            photos = celebration.celebrationphoto_set.all().order_by('order')
            celebration.additional_photos = list(photos)
            celebration.photo_count = len(celebration.additional_photos)
        except:
            celebration.additional_photos = []
            celebration.photo_count = 0
    
    return render(request, 'gallery.html', {'celebration': celebrations})

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
