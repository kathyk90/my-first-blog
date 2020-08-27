from django.db import models

# Create your models here.
from django.utils import timezone
from django_random_queryset import RandomManager


class Persona(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    pin_code = models.CharField(max_length=30, null=True)
    mail = models.EmailField(null=True)


class Question_own(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    objects = RandomManager()
    persona = models.ForeignKey('Persona', on_delete=models.CASCADE, null=True)
   
    
def was_published_recently(self):
   return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question_own, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
