from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image

# Create your views here.
def home(request):
    image = Image.get_images()
    return render(request,'index.html',{"images":image})
def search_results(request):
    pass

def image(request):
    pass

def filter_location(request):
    pass