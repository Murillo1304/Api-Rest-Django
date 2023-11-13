from django.urls import path
from Demo import views

urlpatterns = [
    path('', views.home, name='start'),
]