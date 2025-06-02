from django.urls import path
from. import views
urlpatterns = [
    path('', views.home,name='home'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/',views.contact,name='contact'),
    path('brief/',views.brief,name='brief'),
    path('aboutSchool/',views.aboutSchool,name='aboutSchool'),
    path('chandkheda/',views.chandkheda,name='chandkheda'),
    path('chattral/',views.chattral,name='chattral'),
    path('iffco/',views.iffco,name='iffco'),
    path('kadi/',views.kadi,name='kadi'),
    path('image-test/',views.image_test,name='image_test'),
]

