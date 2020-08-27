from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from child.models import Questions, Choice
from polls.models import Code
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import random

def index(request):
    queryset = Questions.objects.filter(id__in=[1,6])
    latest_question_list = queryset.random() 
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index_2(2).html', context)


def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'detail(2).html', {'question': question})


def answer(request, question_id, key='code'):
    a=[1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Questions, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail(2).html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret)
            return render(request, 'questik(2).html', {'cret': cret})
        else:
            return render(request, 'answer(2).html', {'question': question, 'error_message': 'Ответ неверный!'})
    
def index_2(request):
    queryset = Questions.objects.filter(id__in=[3,4])
    latest_question_list = queryset.random() 
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index_3.html', context)

def detail_2(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'detail_2.html', {'question': question})


def answer_2(request, question_id, key='code'):
    a=[1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Questions, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail_2.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret)
            return render(request, 'quest_2.html', {'cret': cret})
        else:
            return render(request, 'answer_2.html', {'question': question, 'error_message': 'Ответ неверный!'})


def index_3(request):
    queryset = Questions.objects.filter(id__in=[1,5])
    latest_question_list = queryset.random()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index_4.html', context)

def detail_3(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'detail_3.html', {'question': question})


def answer_3(request, question_id, key='code'):
    a=[1,2,3,4,5,6,7,8,9]
    cret_2 = random.choice(a)
    question = get_object_or_404(Questions, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail_3.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret_2)
            return render(request, 'quest/quest.html', {'cret_2': cret_2})
        else:
            return render(request, 'answer_3.html', {'question': question, 'error_message': 'Ответ неверный!'})

