from django.shortcuts import render
from .models import *

def base(request):
    return render(request, "website/base.html")

def about_us(request):
    return render(request, "website/about_us.html")

def articles(request):
    return render(request, "website/articles.html")

def donate(request): 
    return render(request, "website/donate.html")

def contact_us(request):
    return render(request, "website/contact_us.html")

def air(request): 
    return render(request, "website/air.html")

def water(request): 
    return render(request, "website/water.html")

def noise(request): 
    return render(request, "website/noise.html")

def electromagnetic(request): 
    return render(request, "website/electromagnetic.html")

def light(request): 
    return render(request, "website/light.html")

def littering(request): 
    return render(request, "website/littering.html")

def soil_contamination(request): 
    return render(request, "website/soil_contamination.html")

def radioactive_contamination(request): 
    return render(request, "website/radioactive_contamination.html")

def thermal(request): 
    return render(request, "website/thermal.html")

def visual(request): 
    return render(request, "website/visual.html")

def plastic(request): 
    return render(request, "website/plastic.html")

def chat(request): 
    messages = history.objects.all()

    if request.method=="POST":
        message= request.POST.get('message')
        save = history(message=message, anonymous=True)
        save.save()
    return render(request, "website/chat.html", {'messages': messages})
    

