from django.urls import path
from .views import index, retrieve_short_url


urlpatterns = [
    path('', index, name='index'),
    path('<str:shorturl>/', retrieve_short_url, name='shorturl'),
    
]