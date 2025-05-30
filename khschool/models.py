from django.db import models

# Create your models here.
class Celebration(models.Model):
    CELEBRATION_TYPES = [
        ('festival', 'Festival'),
        ('event', 'School Event'),
        ('sports', 'Sports Event'),
        ('cultural', 'Cultural Event'),
        ('academic', 'Academic Event'),
        ('other', 'Other'),
    ]
    
    festivalname = models.CharField(max_length=255, verbose_name='Celebration Name')
    description = models.TextField(blank=True, verbose_name='Description')
    celebration_type = models.CharField(max_length=20, choices=CELEBRATION_TYPES, default='festival', verbose_name='Type')
    image = models.ImageField(upload_to='festival/images/', verbose_name='Main Image')
    date = models.DateTimeField(verbose_name='Date')
    is_featured = models.BooleanField(default=False, verbose_name='Feature on Homepage')
    
    class Meta:
        verbose_name = 'Celebration'
        verbose_name_plural = 'Celebrations'
        ordering = ['-date']
    
    def __str__(self):
        return self.festivalname
        
    def photo_count(self):
        """Return the number of additional photos for this celebration"""
        return self.celebrationphoto_set.count()


class CelebrationPhoto(models.Model):
    """Model for additional photos for a celebration"""
    celebration = models.ForeignKey(Celebration, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='festival/gallery/', verbose_name='Photo')
    caption = models.CharField(max_length=255, blank=True, verbose_name='Caption')
    order = models.IntegerField(default=0, verbose_name='Display Order')
    
    class Meta:
        verbose_name = 'Celebration Photo'
        verbose_name_plural = 'Celebration Photos'
        ordering = ['celebration', 'order']
        
    def __str__(self):
        return f"{self.celebration.festivalname} - Photo {self.order}"

class CarouselImage(models.Model):
    # URL choices for button links
    URL_CHOICES = [
        ('/', 'Home'),
        ('/aboutSchool/', 'About School'),
        ('/brief/', 'Executive Brief'),
        ('/gallery/', 'Gallery'),
        ('/contact/', 'Contact Us'),
        ('/chandkheda/', 'Chandkheda Campus'),
        ('/chattral/', 'Chattral Campus'),
        ('/iffco/', 'IFFCO Campus'),
        ('/kadi/', 'Kadi Campus'),
        ('#', 'No Link (Stay on Page)'),
    ]
    
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='carousel/images/')
    button_text = models.CharField(max_length=50, default='Learn More')
    button_link = models.CharField(max_length=100, choices=URL_CHOICES, default='/')
    order = models.IntegerField(default=0, help_text='Order in which to display the carousel image')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Carousel Image'
        verbose_name_plural = 'Carousel Images'
    
    def __str__(self):
        return self.title