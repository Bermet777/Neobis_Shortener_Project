from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Urls
from .serializers import urlShortenerSerializer
from rest_framework import generics

from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Urls
from .serializers import urlShortenerSerializer
import hashlib

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


def shorten_url(longurl, counter):
  
    hash_code = hashlib.md5(longurl.encode()).hexdigest()

    
    shorturl = f"{hash_code[:6]}{counter:03}"
    return shorturl
