from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')
def search_results(request):
    pass

def image(request):
    pass

def filter_location(request):
    pass