
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from polls.models import Question, Choice, Code
from ris.models import Cret
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import random

def index(request):
    queryset = Question.objects.filter(id__in=[12,13 ])
    latest_question_list = queryset.random() 
    context = {'latest_question_list': latest_question_list}
    return render(request, 'ris/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'ris/detail.html', {'question': question})


def answer(request, question_id):
    a = [1,2,3,4,5,6,7,8,9]
    cret = random.choice(a)
    question = get_object_or_404(Question,pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'ris/detail.html', {'question': question, 'error_message': 'Вы не сделали выбор!'})
    else:
        if choice.correct:
            cod_2 = Code(my_code=cret)
            cod_2.save()
            return render(request, 'ris/ris.html', {'a': a, 'cret': cret})
        else:
            return render(request, 'ris/answer.html', {'question': question, 'error_message': 'Ответ неверный!'})
        
    
