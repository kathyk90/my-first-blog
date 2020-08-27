from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
import random
from django import forms
from django.core.mail import send_mail
from polls.models import Message, Information, Pin, Question, Q, Clas, Choice
from own.models import Question_own, Choice, Persona
from accounts.models import Age
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import Group
import threading




class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/admin/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
    
class LogoutFormView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

def questx(request):
    return render(request, 'polls/index-dark.html')

def info(request):
    return render(request, 'info2.html')


def age(request):
    return render(request, 'age.html')

def quant(request):
    if request.method == 'POST':
        b = request.POST.get('age')
        d = int(b)
        return render(request, 'quant.html', {'d': d})

def message(request):
    k = Age()
    if request.method == 'POST':
        b = request.POST.get('quantity_text')
        c = request.POST.get('age')
        d = int(b)
        f = int(c)
        return render(request, 'message.html', {'d': d, 'f': f})


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()  

def about_user(request):
    a = Age()
    p1 = Message()
    if request.method == 'POST':
        b = request.POST.get('quantity_text')
        c = request.POST.get('age')
        m = request.POST.get('message')
        pin = random.randint(1023, 9976)
        a.age = c
        a.quantity = b
        p1.message_text = m
        p1.save()
        a.message = m
        a.pin = pin
        a.save()
        p = Pin(message_0=p1, pin=pin)
        p.save()
        d =  Age.objects.values()
        j = int(c)
        k = int(b)
        l = m
        return render(request, 'about_user.html', {'d': d, 'pin': pin, 'j': j,'k': k, 'l': l})

def link(request):
    if request.method == 'POST':
        b = request.POST.get('quantity_text')
        c = request.POST.get('age')
        m = request.POST.get('message')
        p = request.POST.get('pin')
        k = Age.objects.values_list('age')
        s = list(k)
        d = s[0]
        l = int(p)
        return render(request, 'link.html', {'l': l, 'p': p, 'k':k})

def link_2(request):
    if request.method == 'POST':
        a = request.POST.get('quantity_text')
        c = request.POST.get('age')
        m = request.POST.get('message')
        p = request.POST.get('pin')
        k = Age.objects.values_list('age')
        s = list(k)
        d = s[0]
        l = int(p)
        quantity = a
        return render(request, 'link_2.html', {'l': l, 'a': a})

def trai(request):
     message_2 = Age.objects.all()
     return render(request, 'go(2).html', {'message_2': message_2})

def trai_2(request):
    if request.method == 'POST':
        p = request.POST.get('pin')
        f = int(p)
        message_2 = Age.objects.values_list()
        return render(request, 'trai.html', {'message_2': message_2})


def tries(request):
    message_2 = Age.objects.values_list('pin', flat=True)
    a = Age.objects.values_list('age', flat=True)
    quantity_text = Age.objects.values_list('quantity', flat=True)
    age = a[0]
    if request.method == 'POST':
        user_pin = request.POST['pin']
        d = str(message_2[0])
        quantity = quantity_text[0]
        if user_pin == d and age == 16 and quantity == 3:
            return render(request, 'tries_2.html')
        elif user_pin == d and age == 16 and quantity == 6:
            return render(request, 'tries_5.html')
        elif user_pin == d and age == 16 and quantity == 9:
            return render(request, 'tries_6.html')
        elif user_pin == d and age == 17 and quantity == 3:
            return render(request, 'tries.html')
        elif user_pin == d and age == 17 and quantity == 6:
            return render(request, 'tries_7.html')
        elif user_pin == d and age == 17 and quantity == 9:
            return render(request, 'tries_8.html')
        else:
            return render(request, 'nonvaliable.html')

def tries_2(request):
    message_2 = Age.objects.values_list('pin', flat=True)
    quantity_text = Age.objects.values_list('quantity', flat=True)
    if request.method == 'POST':
        user_pin = request.POST['pin']
        d = str(message_2[0])
        quantity = quantity_text[0]
        if user_pin == d  and quantity == 6:
            return render(request, 'tries_3.html')
        elif user_pin == d  and quantity == 3:
             return render(request, 'tries_4.html')
            
        else:
            return render(request, 'nonvaliable.html', {'d': d, 'age': age, 'quantity': quantity})


def get_form(request):
    if request.method == 'POST':
        b = request.POST.get('quantity_text')
        c = request.POST.get('age')
        m = request.POST.get('message')
        p = request.POST.get('pin')
        k = int(b)
        j = int(c)
        l = m
        pin = int(p)
    return render(request, 'get_form.html', {'pin': pin, 'k': k, 'j': j, 'l': l})
         
def creation(request):
    z = Persona()
    q = Question_own()
    if request.method == 'POST':
        x = request.POST.get('name')
        y = request.POST.get('mail')
        b = request.POST.get('quantity_text')
        c = request.POST.get('age')
        m = request.POST.get('message')
        p = request.POST.get('pin')
        k = int(b)
        j = int(c)
        l = m
        pin = int(p)
        z = Persona()
        z.first_name = x
        z.mail = y
        z.pin_code = p
        z.save()
        q.question_text = 'test'
        q.pub_date  = '2020-06-24 00:47'
        q.save()
        return render(request, 'create.html', {'pin': pin,'k': k, 'j': j, 'l': l})

def question(request):
    ida = 2
    q = Question_own()
    if request.method == 'POST':
        b = request.POST.get('question')
        c = request.POST.get('choice_1')
        d = request.POST.get('choice_2')
        m = request.POST.get('choice_3')
        qu = request.POST.get('quantity_text')
        a = request.POST.get('age')
        me = request.POST.get('message')
        p = request.POST.get('pin')
        k = int(qu)
        j = int(a)
        l = me
        pin = int(p)
        z = Persona.objects.filter(pin_code=pin).values('id')
        q.question_text = b
        q.pub_date  = '2020-06-24 00:47'
        q.id = ida
        q.persona_id = z
        q.save()
        f = Choice.objects.bulk_create([
        Choice(question=q, choice_text=c, correct=False),
        Choice(question=q, choice_text=d, correct=False),
        Choice(question=q, choice_text=m, correct=True)
            ])
        z3 = Question_own.objects.values()
        return render(request, 'question.html',{'pin': pin, 'k': k, 'j': j, 'l': l})

def question_2(request):
    ida = 3
    q = Question_own()
    if request.method == 'POST':
        b = request.POST.get('question')
        c = request.POST.get('choice_1')
        d = request.POST.get('choice_2')
        m = request.POST.get('choice_3')
        qu = request.POST.get('quantity_text')
        a = request.POST.get('age')
        me = request.POST.get('message')
        p = request.POST.get('pin')
        k = int(qu)
        j = int(a)
        l = me
        pin = int(p)
        z = Persona.objects.filter(pin_code=pin).values('id')
        q.question_text = b
        q.pub_date  = '2020-06-24 00:47'
        q.id = ida
        q.persona_id = z
        q.save()
        f = Choice.objects.bulk_create([
            Choice(question=q, choice_text=c, correct=False),
            Choice(question=q, choice_text=d, correct=True),
            Choice(question=q, choice_text=m, correct=False)
            ])
       
        return render(request, 'question2.html',{'pin': pin, 'k': k, 'j': j, 'l': l})

def question_3(request):
    ida = 1
    q = Question_own()
    if request.method == 'POST':
        b = request.POST.get('question')
        c = request.POST.get('choice_1')
        d = request.POST.get('choice_2')
        m = request.POST.get('choice_3')
        qu = request.POST.get('quantity_text')
        a = request.POST.get('age')
        me = request.POST.get('message')
        p = request.POST.get('pin')
        k = int(qu)
        j = int(a)
        l = me
        pin = int(p)
        z = Persona.objects.filter(pin_code=pin).values('id')
        q.question_text = b
        q.pub_date  = '2020-06-24 00:47'
        q.id = ida
        q.persona_id = z
        q.save()    
        f = Choice.objects.bulk_create([
            Choice(question=q, choice_text=c, correct=True),
            Choice(question=q, choice_text=d, correct=False),
            Choice(question=q, choice_text=m, correct=False)
            ])
        return render(request, 'question3.html',{'pin': pin, 'k': k, 'j': j, 'l': l})

def question_4(request):
    ida = 5
    q = Question_own()
    if request.method == 'POST':
        b = request.POST.get('question')
        c = request.POST.get('choice_1')
        d = request.POST.get('choice_2')
        m = request.POST.get('choice_3')
        qu = request.POST.get('quantity_text')
        a = request.POST.get('age')
        me = request.POST.get('message')
        p = request.POST.get('pin')
        k = int(qu)
        j = int(a)
        l = me
        pin = int(p)
        z = Persona.objects.filter(pin_code=pin).values('id')
        if k == 3:
            return render(request, 'fine.html',{'pin': pin, 'k': k, 'j': j, 'l': l})
        else:
            q.question_text = b
            q.pub_date  = '2020-06-24 00:47'
            q.id = ida
            q.persona_id = z
            q.save()
            f = Choice.objects.bulk_create([
            Choice(question=q, choice_text=c, correct=False),
            Choice(question=q, choice_text=d, correct=False),
            Choice(question=q, choice_text=m, correct=True)
            ])
            return render(request, 'question4.html',{'pin': pin, 'k': k, 'j': j, 'l': l})

def question_5(request):
    ida = 6
    q = Question_own()
    if request.method == 'POST':
        b = request.POST.get('question')
        c = request.POST.get('choice_1')
        d = request.POST.get('choice_2')
        m = request.POST.get('choice_3')
        qu = request.POST.get('quantity_text')
        a = request.POST.get('age')
        me = request.POST.get('message')
        p = request.POST.get('pin')
        k = int(qu)
        j = int(a)
        l = me
        pin = int(p)
        z = Persona.objects.filter(pin_code=pin).values('id')
        q.question_text = b
        q.pub_date  = '2020-06-24 00:47'
        q.id = ida
        q.persona_id = z
        q.save()
        f = Choice.objects.bulk_create([
            Choice(question=q, choice_text=c, correct=True),
            Choice(question=q, choice_text=d, correct=False),
            Choice(question=q, choice_text=m, correct=False)
            ])

        return render(request, 'question5.html',{'pin': pin, 'k': k, 'j': j, 'l': l})

def question_6(request):
    q = Question_own()
    ida = 4
    if request.method == 'POST':
        b = request.POST.get('question')
        c = request.POST.get('choice_1')
        d = request.POST.get('choice_2')
        m = request.POST.get('choice_3')
        qu = request.POST.get('quantity_text')
        a = request.POST.get('age')
        me = request.POST.get('message')
        p = request.POST.get('pin')
        k = int(qu)
        j = int(a)
        l = me
        pin = int(p)
        z = Persona.objects.filter(pin_code=pin).values('id')
        q.question_text = b
        q.pub_date  = '2020-06-24 00:47'
        q.id = ida
        q.persona_id = z
        q.save()
        f = Choice.objects.bulk_create([
            Choice(question=q, choice_text=c, correct=False),
            Choice(question=q, choice_text=d, correct=True),
            Choice(question=q, choice_text=m, correct=False)
            ])
       
        return render(request, 'question6.html',{'pin': pin, 'k': k, 'j': j, 'l': l})


def fine(request):
    z = Persona()
    q = Question_own()
    r = Persona.objects.values_list('first_name')
    t = Persona.objects.values_list('mail')
    o = Persona.objects.values_list('pin_code')
    if request.method == 'POST':
        b = request.POST.get('quantity_text')
        c = request.POST.get('age')
        m = request.POST.get('message')
        p = request.POST.get('pin')
        k = int(b)
        j = int(c)
        l = m
        pin = int(p)
        return render(request, 'fine.html', {'pin': pin, 'k': k, 'j': j, 'l': l})
    
        
def contacts(request):
    return render(request, 'contacts.html')

    
        
    
        
    
        
        

        
