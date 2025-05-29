from django.shortcuts import render
from django.http import HttpResponse
from .models import Celebration
# Create your views here.
def home(request):
    return render(request,'home.html')

#gallery page
def gallery(request):
    celebrations = Celebration.objects.all()
    return render(request,'gallery.html',{'celebration':celebrations})

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
