from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from child.models import Questions, Choice
from own.models import Question_own, Choice, Persona
from polls.models import Code
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import random
from accounts.models import Age

def own_hello_3(request):
    return render(request, 'polls/hello_3.html')  

def index(request):
    if request.method == 'POST':
        p = request.POST.get('pin')
        y = str(p)
        z = Persona.objects.filter(pin_code=p).values_list('id')
        b = Code.objects.all()
        b.delete()
        k = list(z[0])
        m = str(k[0])
        q = Question_own.objects.filter(persona_id=m,id=4)
        latest_question_list = q
        request.session["pid"] = m
        context = {'latest_question_list': latest_question_list}
        return render(request, 'polls/index_5.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question_own, pk=question_id)
    return render(request, 'detail_own.html', {'question': question})
    


def answer(request, question_id):
    a=[1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Question_own, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail_own.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret)
            return render(request, 'own_q.html', {'cret': cret})
        else:
            return render(request, 'answer_own.html', {'question': question, 'error_message': 'Ответ неверный!'})
      
def index_2(request):
    m = request.session["pid"]
    latest_question_list =  Question_own.objects.filter(id=2, persona_id=m)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index_6.html', context)

def detail_2(request, question_id):
    question = get_object_or_404(Question_own, pk=question_id)
    return render(request, 'detail_own_2.html', {'question': question})


def answer_2(request, question_id, key='code'):
    a=[1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Question_own, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail_own_2.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret)
            return render(request, 'own_q_2.html', {'cret': cret})
        else:
            return render(request, 'answer_own_2.html', {'question': question, 'error_message': 'Ответ неверный!'})


def index_3(request):
    m = request.session["pid"]
    q = Question_own.objects.filter(id=6, persona_id=m)
    latest_question_list = q
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index_7.html', context)

def detail_3(request, question_id):
    question = get_object_or_404(Question_own, pk=question_id)
    return render(request, 'detail_own_3.html', {'question': question})


def answer_3(request, question_id):
    a=[1,2,3,4,5,6,7,8,9]
    cret_2 = random.choice(a)
    question = get_object_or_404(Question_own, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail_own_3.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret_2)
            return render(request, 'own_q_3.html', {'cret_2': cret_2})
        else:
            return render(request, 'answer_own_3.html', {'question': question, 'error_message': 'Ответ неверный!'})
def index_4(request):
    m = request.session["pid"]
    q = Question_own.objects.filter(id=1, persona_id=m)
    latest_question_list = q
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index_8.html', context)


def detail_4(request, question_id):
    question = get_object_or_404(Question_own, pk=question_id)
    return render(request, 'detail_own_4.html', {'question': question})


def answer_4(request, question_id):
    a=[1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Question_own, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail_own_4.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret)
            return render(request, 'own_q_4.html', {'cret': cret})
        else:
            return render(request, 'answer_own_4.html', {'question': question, 'error_message': 'Ответ неверный!'})
      
def index_5(request):
    m = request.session["pid"]
    q = Question_own.objects.filter(id=5, persona_id=m)
    latest_question_list = q
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index_9.html', context)

def detail_5(request, question_id):
    question = get_object_or_404(Question_own, pk=question_id)
    return render(request, 'detail_own_5.html', {'question': question})


def answer_5(request, question_id):
    a=[1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Question_own, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail_own_5.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret)
            return render(request, 'own_q_5.html', {'cret': cret})
        else:
            return render(request, 'answer_own_5.html', {'question': question, 'error_message': 'Ответ неверный!'})


def index_6(request):
    m = request.session["pid"]
    q = Question_own.objects.filter(id=3, persona_id=m)
    latest_question_list = q
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index_10.html', context)

def detail_6(request, question_id):
    question = get_object_or_404(Question_own, pk=question_id)
    return render(request, 'detail_own_6.html', {'question': question})


def answer_6(request, question_id):
    a=[1,2,3,4,5,6,7,8,9]
    cret_2 = random.choice(a)
    question = get_object_or_404(Question_own, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail_own_6.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            q = Question_own.objects.all()
            q.delete()
            cod_1 = Code.objects.create(my_code=cret_2)
            return render(request, 'quest/quest.html', {'cret_2': cret_2})
        else:
            return render(request, 'answer_own_6.html', {'question': question, 'error_message': 'Ответ неверный!'})

def test(request):
    z = Persona.objects.values()
    q = Question_own.objects.values()
    p = Persona_2.objects.values('p_id')
    return render(request, 'test.html', {'z': z, 'q':q, 'p':p})
