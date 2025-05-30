from django.contrib import admin
from khschool.models import Celebration, CarouselImage, CelebrationPhoto

# Register your models here.

class CelebrationPhotoInline(admin.TabularInline):
    model = CelebrationPhoto
    extra = 3  # Show 3 empty forms for adding photos
    fields = ('photo', 'caption', 'order')

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')

@admin.register(Celebration)
class CelebrationAdmin(admin.ModelAdmin):
    list_display = ('festivalname', 'celebration_type', 'date', 'photo_count_display', 'preview_image')
    list_filter = ('date', 'celebration_type', 'is_featured')
    search_fields = ('festivalname', 'description')
    date_hierarchy = 'date'
    ordering = ('-date',)
    inlines = [CelebrationPhotoInline]
    
    def preview_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />'
        return 'No Image'
    
    def photo_count_display(self, obj):
        count = obj.photo_count()
        return f'{count} photo{"s" if count != 1 else ""}'
    
    preview_image.allow_tags = True
    preview_image.short_description = 'Image Preview'
    photo_count_display.short_description = 'Additional Photos'

@admin.register(CelebrationPhoto)
class CelebrationPhotoAdmin(admin.ModelAdmin):
    list_display = ('celebration', 'caption', 'order', 'preview_photo')
    list_filter = ('celebration',)
    list_editable = ('order',)
    search_fields = ('celebration__festivalname', 'caption')
    
    def preview_photo(self, obj):
        if obj.photo:
            return f'<img src="{obj.photo.url}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />'
        return 'No Image'
    
    preview_photo.allow_tags = True
    preview_photo.short_description = 'Photo Preview'