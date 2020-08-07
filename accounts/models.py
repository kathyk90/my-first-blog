from django.db import models
from django.contrib.auth.models import User


class Age(models.Model):
      age =  models.IntegerField(null=True)
      pin = models.IntegerField(null=True)
      message = models.CharField(max_length=2000, null=True)
      quantity = models.IntegerField(null=True)
      
      def __init__(self='', age='', pin='', message='', quantity='', **kwargs):
            self.age = age
            self.pin = pin
            self.message = message
            self.quantity = quantity
            super().__init__(**kwargs)   
      
