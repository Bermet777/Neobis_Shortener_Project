from django.urls import path
from .views import index, retrieve_original_url

urlpatterns = [
    path('', index, name='index'),
    path('<str:shorturl>/', retrieve_original_url, name='longurl'),
]