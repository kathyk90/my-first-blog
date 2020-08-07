from django.shortcuts import render
import random
import requests
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.

def tot(request):
    dict = {'cod':'123'}
    if request.method == 'POST':
        user_cod = request.POST['cod']
        if cod in dict.values():
            return render(request, 'tot/cod.html')
        else:
            return render(request, 'tot/tot.html', {'cod': cod})
    
    
            
def breakage(c):
     if c == '123':
           return render(c, 'tot/code.html')
     else:
           return render(c, 'ris/ris.html')
         
