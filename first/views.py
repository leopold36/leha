from django.http import HttpResponse
from django.shortcuts import render
from .models import Entity

# Create your views here.
def index(request):
    context = {
        "entity": Entity.objects.all()
    }
        
    return render(request, "entity/index.html", context)
     
     