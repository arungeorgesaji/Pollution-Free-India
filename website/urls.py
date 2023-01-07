from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

urlpatterns =[
    path('', views.base, name="base"),
    path('about_us/', views.about_us, name="about_us")
]

urlpatterns += staticfiles_urlpatterns()