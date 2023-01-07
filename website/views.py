from django.shortcuts import render

def base(request):
    return render(request, "website/base.html")

def about_us(request):
    return render(request, "website/about_us.html")
