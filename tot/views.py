from django.shortcuts import get_object_or_404, render
from django.http import Http404
import random
import requests
from polls.models import Code, Message
from accounts.models import Age
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def tot(request):
     dic = Code.objects.values_list('my_code', flat=True)
     if request.method == 'POST':
        user_cod = request.POST['cod']
        d_2 = dic
        global d
        d = str("".join(d_2))
        if user_cod == d:
             return render(request, 'tot/code.html')                  
        else:
             return render(request, 'tot/cod.html', {'d_2': d_2})
    
            
def breakage(request):
     if request.method == 'POST':
          user_cod = request.POST['cod']
          d_2 = request.POST['code']
          if user_cod == d:
               return render(request, 'tot/code.html')   
          else:
               return render(request, 'tot/last.html', {'d_2': d_2})
          
def last_chance(request):
     if request.method == 'POST':
          user_cod = request.POST['cod']
          if user_cod == d:
                return render(request, 'tot/code.html')   
          else:
               chance = Code.objects.all()
               chance.delete()
               return render(request, 'tot/sorry.html')
          
     

def total(request):
     total = Code.objects.all()
     total.delete()
     age = Age.objects.values_list('message', flat=True)
     a  = age[0]
     return render(request, 'tot/present.html', {'a': a})
  
