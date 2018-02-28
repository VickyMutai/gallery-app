from django.contrib import admin
from .models import Category,Image,Location

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('category','location')

# Register your models here.
admin.site.register(Category)
admin.site.register(Image,ImageAdmin)
admin.site.register(Location)
