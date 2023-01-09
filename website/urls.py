from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

urlpatterns =[
    path('', views.base, name="base"),
    path('about_us/', views.about_us, name="about_us"),
    path('articles/', views.articles, name="articles"),
    path('donate/', views.donate, name="donate"),
    path('contact_us/', views.contact_us, name="contact"),
    path('air_pollution/', views.air, name="air"),
    path('water_pollution/', views.water, name="water"),
    path('noise_pollution/', views.noise, name="noise"),
    path('littering/', views.littering, name="littering"),
    path('electromagnetic_pollution/', views.electromagnetic, name="electromagnetic"),
    path('soil_contamination/', views.soil_contamination, name="soil_contamination"),
    path('radioactive_contamination/', views.radioactive_contamination, name="radioactive_contamination"),
    path('light_pollution/', views.light, name="light"),
    path('thermal_pollution/', views.thermal, name="thermal"),
    path('visual_pollution/', views.visual, name="visual"),
    path('plastic_pollution/', views.plastic, name="plastic"),
]

urlpatterns += staticfiles_urlpatterns()