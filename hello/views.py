from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from accounts.models import Age

def quest(request):
    return render(request, 'quest.html')


def tipe(request):
    return render(request, 'polls/index-dark.html')

def tipe_2(request):
    return render(request, 'accounts/trai.html')
        
def creat(request):
    return render(request, 'info.html')

def go(request):
    return render(request, 'go(2).html')

def hello(request):
    return render(request, 'polls/hello.html')
       
            
def hello_2(request):
    return render(request, 'polls/hello_2.html')

    
def hello_3(request):
    return render(request, 'polls/hello_3.html')    
   
def hello_4(request):
    return render(request, 'polls/hello_4.html')

def hello_5(request):
    return render(request, 'polls/hello_5.html')

def hello_6(request):
    return render(request, 'polls/hello_6.html')

def hello_7(request):
    return render(request, 'polls/hello_7.html')

def hello_8(request):
    return render(request, 'polls/hello_8.html')  
