

# Create your views here.
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

def index(request):
    b = Code.objects.all()
    b.delete()
    queryset = Questions.objects.filter(id__in=[5,6])
    latest_question_list = queryset.random()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index_25.html', context)


def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'ch_detail_own.html', {'question': question})


def answer(request, question_id):
    a=[1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Questions, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'ch_detail_own.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret)
            return render(request, 'ch_own_q_1.html', {'cret': cret})
        else:
            return render(request, 'ch_answer_own.html', {'question': question, 'error_message': 'Ответ неверный!'})
      
def index_2(request):
    queryset = Questions.objects.filter(id__in=[1,2])
    latest_question_list = queryset.random()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index_26.html', context)

def detail_2(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'ch_detail_own_2.html', {'question': question})


def answer_2(request, question_id, key='code'):
    a=[1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Questions, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'ch_detail_own_2.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret)
            return render(request, 'ch_own_q_2.html', {'cret': cret})
        else:
            return render(request, 'ch_answer_own_2.html', {'question': question, 'error_message': 'Ответ неверный!'})


def index_3(request):
    queryset = Questions.objects.filter(id__in=[2,3])
    latest_question_list = queryset.random()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index_27.html', context)

def detail_3(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'ch_detail_own_3.html', {'question': question})


def answer_3(request, question_id):
    a=[1,2,3,4,5,6,7,8,9]
    cret_2 = random.choice(a)
    question = get_object_or_404(Questions, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'ch_detail_own_3.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret_2)
            return render(request, 'ch_own_q_3.html', {'cret_2': cret_2})
        else:
            return render(request, 'ch_answer_own_3.html', {'question': question, 'error_message': 'Ответ неверный!'})
def index_4(request):
    queryset = Questions.objects.filter(id__in=[4,5])
    latest_question_list = queryset.random()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index_28.html', context)


def detail_4(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'ch_detail_own_4.html', {'question': question})


def answer_4(request, question_id):
    a=[1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Questions, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'ch_detail_own_4.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret)
            return render(request, 'ch_own_q_4.html', {'cret': cret})
        else:
            return render(request, 'ch_answer_own_4.html', {'question': question, 'error_message': 'Ответ неверный!'})
      
def index_5(request):
    queryset = Questions.objects.filter(id__in=[1,3])
    latest_question_list = queryset.random()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index_29.html', context)

def detail_5(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'ch_detail_own_5.html', {'question': question})


def answer_5(request, question_id):
    a=[1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Questions, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'ch_detail_own_5.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret)
            return render(request, 'ch_own_q_5.html', {'cret': cret})
        else:
            return render(request, 'ch_answer_own_5.html', {'question': question, 'error_message': 'Ответ неверный!'})


def index_6(request):
    queryset = Questions.objects.filter(id__in=[2,6])
    latest_question_list = queryset.random()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index_20.html', context)

def detail_6(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'ch_detail_own_6.html', {'question': question})


def answer_6(request, question_id):
    a=[1,2,3,4,5,6,7,8,9]
    cret_2 = random.choice(a)
    question = get_object_or_404(Questions, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'ch_detail_own_6.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret_2)
            return render(request, 'quest/quest.html', {'cret_2': cret_2})
        else:
            return render(request, 'ch_answer_own_6.html', {'question': question, 'error_message': 'Ответ неверный!'})

        
