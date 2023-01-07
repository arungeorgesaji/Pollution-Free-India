from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

urlpatterns =[
    path('', views.base, name="base"),
    path('about_us/', views.about_us, name="about_us"),
    path('articles/', views.articles, name="articles"),
    path('pollution_types/', views.pollutions, name="pollution"),
    path('donate/', views.donate, name="donate"),
    path('contact_us/', views.contact_us, name="contact"),
]

urlpatterns += staticfiles_urlpatterns()