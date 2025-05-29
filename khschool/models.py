from django.db import models

# Create your models here.
class Celebration(models.Model):
    festivalname = models.CharField(max_length=255)
    image=models.ImageField(upload_to='festival/images/')
    date= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.festivalname