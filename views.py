from django.shortcuts import render,redirect,reverse
from .models import *
from django.contrib.auth.models import Group
from django.http import HttpResponse

from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404

from django.db.models import Count, F, Value,Min,Sum
from .forms import PostForm,QuestForm,UserqForm,AnqForm
from .CreditCardField import PaymentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views import View

from django.contrib.auth import logout

from .decorators import admin_only,admin_only1
from django.http import HttpResponseRedirect

def index(request):
	context = {}
	return render(request, 'tickets/index.html', context)
@login_required(login_url='/login')
def ticket_new(request):
	#form	
	if request.method=="POST":
		form=PostForm(request.POST)
		if(form.is_valid()):
			new=form.save()
			print(new.pk)
			return render(request,"tickets/payment.html",{'form':form,'pk':new.pk})
	else:
		form=PostForm()
		return render (request,"tickets/ticket_new.html",{'form':form})
@login_required(login_url='/login')
def payment(request):
	
	return render(request,"tickets/payment.html")

@login_required(login_url='/login')

def level_list(request):
	levels=ticket.objects.values('level').distinct().annotate(occurrences=Count('level'), pk=Min('pk'))
	status=ticket.objects.all()
	total=0
	for x in status:
		if x.pay==True:
			total=total+x.num
	#total=list(ticket.objects.aggregate(Sum('num')).values())[0]
	return render(request,"tickets/level_list.html",{"levels":levels,"total":total})
@login_required(login_url='/login')

def level_detail(request,level):
	levels=ticket.objects.filter(level=level).all()
	return render(request,"tickets/level_detail.html",{"levels":levels,"lev":level})
@login_required(login_url='/login')

def studentdetails(request,pk):
	det=ticket.objects.get(pk=pk)
	return render(request,"tickets/studentdetails.html",{"det":det})
@login_required(login_url='/login')
def doubt(request):
	qq=question.objects.all()
	
	return render(request,"tickets/doubt.html",{"qq":qq})


@login_required(login_url='/login')
@admin_only
def faq(request):
	if request.method=="POST":
		form=QuestForm(request.POST)
		if(form.is_valid()):
			form.save()
			return redirect('doubt')
	else:
		form=QuestForm()
		return render (request,"tickets/faq.html",{'form':form})
@login_required(login_url='/login')
@admin_only
def question_remove(request, pk):
    q=get_object_or_404(optq, pk=pk)
    q.delete()
    return redirect('question_new')
@login_required(login_url='/login')
@admin_only1
def faq_remove(request, pk):
    q=get_object_or_404(question, pk=pk)
    q.delete()
    return redirect('doubt')
	


	
	
	
@login_required(login_url='/login')
def ansquestion(request,pk):
	
	
	rec=optq.objects.get(pk=pk)
	
	if request.method=="POST":
		form=AnqForm(request.POST,instance=rec)
		
		if(form.is_valid()):
			
			form.save()
			return redirect('question_new')
	else:
		
		form=AnqForm(instance=rec)
		return render(request,"tickets/ansquestion.html",{"form":form})
	
	
	
@login_required(login_url='/login')
def question_new(request):
	if request.method=="POST":
		form=UserqForm(request.POST)
		if(form.is_valid()):
			form.save()
			
	else:
		form=UserqForm()
	uq=optq.objects.all()
	return render (request,"tickets/question_new.html",{'form':form,'uq':uq})
		
@login_required(login_url='/login')		
def credit(request,pk):

	rec=ticket.objects.get(pk=pk)
	if request.method=="POST":
		form=PaymentForm(request.POST)
		if(form.is_valid()):
			
			rec.pay=True
			rec.save()
			return render(request,"tickets/success.html",{"form":form,"rec":rec})
		else:
			return render(request,"tickets/credit.html",{"form":form,"invalid_creds":True})
	else:
		form=PaymentForm()
		
		return render(request,"tickets/credit.html",{"form":form,"invalid_creds":True})
		
		





@login_required(login_url='/login')
def success(request):
	return render(request,"tickets/success.html")
	
def register(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		print(form.errors)
		if form.is_valid():
			form.save()
			return redirect("registered")
		else:
			return redirect("register")
	return render(request,"tickets/register.html",{"form":UserCreationForm()})
	
def registered(request):
	return render(request,"tickets/registered.html")	

class LoginView(View):
	def get(self,request):
		return render(request,"tickets/login.html",{"form":AuthenticationForm()})
	def post(self,request):
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			print ("login logic")
			user = authenticate(request,username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
			print(user)
			if user is None:
				
				return redirect(request,"login.html",{"form":form,"invalid_creds":True})
			login(request, user)
			return redirect(reverse('index'))
	
		else:
			print ("invalid login")
			return render(request,"tickets/login.html",{"form":form,"invalid_creds":True})
def logout_request(request):
	logout(request)
	messages.info(request,"Logged out successfully!")
	return render(request,"tickets/index.html")


