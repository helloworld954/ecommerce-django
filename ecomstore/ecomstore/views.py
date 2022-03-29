
from unicodedata import name
from django.http import HttpResponse
from django.template.loader import get_template

def catalog(request): 
    my_context = { 'site_name': 'Modern Musician 2' }
    response_html = get_template('sample.html').render(my_context)
    return HttpResponse(response_html)