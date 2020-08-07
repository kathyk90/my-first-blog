import datetime

from django.db import models
from django.utils import timezone
from django_random_queryset import RandomManager


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    objects = RandomManager()
    own = models.CharField(max_length=200, null=True)
    
   
    

def was_published_recently(self):
   return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

class Code(models.Model):
    my_code = models.CharField(max_length=200)
    cod_2 = models.CharField(max_length=200)
    cod_3 = models.CharField(max_length=200)
    
class Message(models.Model):
    message_text = models.CharField(max_length=2000, null=True)
    

class Information(models.Model):
    name = models.CharField(max_length=200, null=True)
    age =  models.CharField(max_length=200, null=True)
    
class Pin(models.Model):
    user_name = models.OneToOneField(Information, on_delete=models.CASCADE, null=True)
    pin = models.CharField(max_length=200, null=True)
    message_0 = models.OneToOneField(Message, on_delete=models.CASCADE, null=True)
    

class Q(models.Model):
    quantity = models.CharField(max_length=200)
    
class Clas(models.Model):
    user_quantity = models.ForeignKey(Q, on_delete=models.CASCADE)
    quantity_text = models.CharField(max_length=200, null=True)


    
