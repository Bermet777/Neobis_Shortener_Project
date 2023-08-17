from django.urls import path
from .views import index, retrieve_original_url, retrieve_shorturl


urlpatterns = [
    path('', index, name='index'),
    path('<str:shorturl>/', retrieve_original_url, name='longurl'),
    path('retrieve/', retrieve_shorturl, name='retrieve_shorturl'),
]