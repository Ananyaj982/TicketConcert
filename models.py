#pip install django-credit-cards

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date, datetime
from calendar import monthrange
from django import forms


lev= ( 
    ("Premium", "Premium"), 
    ("Executive", "Executive"), 
    ("Regular", "Regular"), 
    
)
b=(
	("CSE","CSE"),
	("ECE","ECE"),
	("EEE","EEE"),
	("BT","BT"),
	("CV","CV"),
	("ME","ME"),
	("OTHERS","OTHERS"),
)

class ticket(models.Model):

	name=models.TextField()
	branch=models.CharField(
		max_length = 20, 
        choices = b, 
        default = '...'
		
	)
	level=models.CharField(
	 
        max_length = 20, 
        choices = lev, 
        default = '1'
	)
	num=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
	pay= models.BooleanField(default=False)

	

	def __str__(self):
		return self.name
class question(models.Model):
	quest=models.TextField()	
	an=models.TextField()
	def __str__(self):
		return self.quest
		
class optq(models.Model):
	userq=models.TextField()
	anq=models.TextField(default='n/a')


	

	