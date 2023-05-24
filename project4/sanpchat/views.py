from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def envy(request):
    return render(request,'new.html')
