
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Choice, Code
from own.models import Question_own, Choice
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import random


def index(request):
    queryset = Question.objects.filter(id__in=[1,2,3,4,5,6])
    latest_question_list = queryset.random() 
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def index_2(request):
    q = Question_own.objects.filter(id__in=[1,2,3,4,5,6])
    latest_question_list = random.sample(list(q),k=1)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def answer(request, question_id, key='code'):
    a=[1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_1 = Code.objects.create(my_code=cret)
            return render(request, 'polls/quest.html', {'cret': cret})
        else:
            return render(request, 'polls/answer.html', {'question': question, 'error_message': 'Ответ неверный!'})
          
    
