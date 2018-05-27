from django.http import HttpResponse
from django.shortcuts import render
from .models import Entity, Group

# Create your views here.
def index(request):
    context = {
        "Group": Group.objects.all()
    }
        
    return render(request, "entity/index.html", context)
     
     