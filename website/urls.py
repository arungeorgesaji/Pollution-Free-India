from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

urlpatterns =[
    path('', views.base, name="base"),
]

urlpatterns += staticfiles_urlpatterns()