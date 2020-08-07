from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from child.models import Questions, Choice
from own.models import Question_own, Choice
from polls.models import Code
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import random


# Create your views here.
def index(request):
    b = Code.objects.all()
    b.delete()
    queryset = Question_own.objects.all()[0:2]
    latest_question_list = random.sample(set(queryset), 1)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index_15.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question_own, pk=question_id)
    return render(request, 'polls/q_detail_own.html', {'question': question})


def answer(request, question_id):
    a=[1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Question_own, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/q_detail_own.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret)
            return render(request, 'polls/q_own_q.html', {'cret': cret})
        else:
            return render(request, 'polls/q_answer_own.html', {'question': question, 'error_message': 'Ответ неверный!'})
      
def index_2(request):
    queryset = Question_own.objects.all()[2:4]
    latest_question_list = random.sample(set(queryset), 1)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index_16.html', context)

def detail_2(request, question_id):
    question = get_object_or_404(Question_own, pk=question_id)
    return render(request, 'polls/q_detail_own_2.html', {'question': question})


def answer_2(request, question_id, key='code'):
    a=[1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Question_own, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/q_detail_own_2.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret)
            return render(request, 'polls/q_own_q_2.html', {'cret': cret})
        else:
            return render(request, 'polls/q_answer_own_2.html', {'question': question, 'error_message': 'Ответ неверный!'})


def index_3(request):
    queryset = Question_own.objects.all()[4:6]
    latest_question_list = random.sample(set(queryset), 1)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index_17.html', context)

def detail_3(request, question_id):
    question = get_object_or_404(Question_own, pk=question_id)
    return render(request, 'polls/q_detail_own_3.html', {'question': question})


def answer_3(request, question_id):
    a=[1,2,3,4,5,6,7,8,9]
    cret_2 = random.choice(a)
    question = get_object_or_404(Question_own, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/q_detail_own_3.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            q = Question_own.objects.all()
            q.delete()
            cod_1 = Code.objects.create(my_code=cret_2)
            return render(request, 'quest/quest.html', {'cret_2': cret_2})
        else:
            return render(request, 'polls/answer_own_3.html', {'question': question, 'error_message': 'Ответ неверный!'})
