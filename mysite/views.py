from django.http import HttpResponse
from django.shortcuts import render
from slide.models import Slide
# Create your views here.
def index(request):
    slides = Slide.objects.all()
    return render(request, 'index.html',{'slides':slides})