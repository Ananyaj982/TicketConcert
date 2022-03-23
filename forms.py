from django import forms
from .models import ticket
from .models import question
from .models import optq
class PostForm(forms.ModelForm):
	class Meta:
		model=ticket
		fields=('name','branch','level','num')
class QuestForm(forms.ModelForm):
	class Meta:
		model=question
		fields=('quest','an')
		
		
class UserqForm(forms.ModelForm):
	class Meta:
		model=optq
		fields=('userq',)
class AnqForm(forms.ModelForm):
	class Meta:
		model=optq
		fields=('anq',)
		
		

		
