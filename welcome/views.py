from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def plus(request):
    
    return render(request,"Welcome.html")