from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Urls
from .serializers import urlShortenerSerializer
from rest_framework import generics

import random

# class ShortenedURLCreateView(generics.CreateAPIView):
#     queryset = Urls.objects.all()
#     serializer_class = urlShortenerSerializer

# class ShortenedURLRetrieveView(generics.RetrieveAPIView):
#     queryset = Urls.objects.all()
#     serializer_class = urlShortenerSerializer
#     lookup_field = 'short_code'

# urlshortener_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Urls
from .serializers import urlShortenerSerializer
import hashlib
# Counter to ensure uniqueness of short codes
url_counter = 0

@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def index(request):
    global url_counter

    if request.method == 'POST':
        longurl = request.data.get('longurl')
        shorturl = shorten_url(longurl, url_counter)
        shortened_url = Urls.objects.create(longurl=longurl, shorturl=shorturl)
        url_counter += 1
        return redirect('longurl', shorturl=shortened_url.shorturl)

    return Response({'message': 'Welcome to the URL Shortener API'}, template_name='index.html')

@api_view(['GET'])
def retrieve_original_url(request, shorturl):
    shortened_url = get_object_or_404(Urls, shorturl=shorturl)
    serializer = urlShortenerSerializer(shortened_url)
    return Response(serializer.data)

# Updated URL shortening function to ensure uniqueness
def shorten_url(longurl, counter):
    # Generate a hash of the original URL
    hash_code = hashlib.md5(longurl.encode()).hexdigest()

    # Append counter and random characters to ensure uniqueness
    shorturl = f"{hash_code[:6]}{counter:03}"
    return shorturl

@api_view(['GET', 'POST'])
def retrieve_shorturl(request):
    if request.method == 'POST':
        shorturl = request.data.get('shorturl')
        try:
            shortened_url = Urls.objects.get(shorturl=shorturl)
            original_url = shortened_url.longurl
        except Urls.DoesNotExist:
            original_url = None

        return render(request, 'retrieve_shorturl.html', {'original_url': original_url})

    return render(request, 'retrieve_shorturl.html')