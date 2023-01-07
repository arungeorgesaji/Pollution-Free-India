from django.shortcuts import render

def base(request):
    return render(request, "website/base.html")

def about_us(request):
    return render(request, "website/about_us.html")

def articles(request):
    return render(request, "website/articles.html")

def pollutions(request):
    return render(request, "website/pollutions.html")

def donate(request): 
    return render(request, "website/donate.html")

def contact_us(request):
    return render(request, "website/contact_us.html")
