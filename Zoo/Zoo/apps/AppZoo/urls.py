from django.urls import path

from . import views

app_name = 'Zoo'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('animals/', views.animals, name = 'animals'),
    
]
