from django.shortcuts import render, get_object_or_404
from django import forms
from .models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.template import RequestContext
#import requests 
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template,RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from itertools import chain

# Create your views here.
ids=[]
def create_interview_page(request):
	if request.method == 'POST':
		form=DetailsForm(request.POST)	
		if form.is_valid():
			inter_id=form.cleaned_data['interview_id']
			start_time=form.cleaned_data['start_time']
			end_time=form.cleaned_data['end_time']
			interviewee_email=form.cleaned_data['interviewee_email']
			interviewer_email=form.cleaned_data['interviewer_email']

			userdetails= User_Detail.objects.all()
			found1=0
			found2=0
			for user in userdetails.values('email'):
				email_id=user['email']
				if interviewee_email==email_id:
					found1=1
				if interviewer_email==email_id:
					found2=1
			if found1==0 or found2==0:
				return HttpResponse("Sorry this email_id is not present in our database, aborting interview scheduling!!")

			cant_be_done1=0
			cant_be_done2=0
			allinterviewdetails_interviewer=Interviewer.objects.filter(email=interviewer_email)
			allinterviewdetails_candidate=Interviewee.objects.filter(email=interviewee_email)
			for user in allinterviewdetails_interviewer.values('interview_id'):
				Id=user['interview_id']
				user_all_interviews=InterviewCreation.objects.filter(interview_id=Id)
				for timee in user_all_interviews.values('start_time','end_time'):
					st_time=timee['start_time']
					en_time=timee['end_time']
					if start_time>= st_time and start_time<=en_time:
						cant_be_done1=1
						break
				if cant_be_done1==1:
					break
			for user in allinterviewdetails_candidate.values('interview_id'):
				Id=user['interview_id']
				user_all_interviews=InterviewCreation.objects.filter(interview_id=Id)
				for timee in user_all_interviews.values('start_time','end_time'):
					st_time=timee['start_time']
					en_time=timee['end_time']
					if start_time>= st_time and start_time<=en_time:
						cant_be_done2=1
						break
				if cant_be_done2==1:
					break

			if cant_be_done1==1:
				return HttpResponse("sorry, interviewer is busy")

			if cant_be_done2==1:
				return HttpResponse("sorry, candidate is busy")


			Int_Create=InterviewCreation(interview_id=inter_id, interviewee_email=interviewee_email, interviewer_email=interviewer_email , start_time=start_time, end_time=end_time)
			Int_Create.save()
			
			int_id=InterviewCreation.objects.get(interview_id=inter_id)
			I=Interviewer(email=interviewer_email, interview_id=int_id)
			I.save()	
			C=Interviewee(email=interviewee_email, interview_id=int_id)
			C.save()
			return HttpResponse("successfully_saved")

	else:
		form=DetailsForm()

	return render(request, 'scheduling_interview/create.html', {'form': form})


def list_interview_details(request):
	queryset=InterviewCreation.objects.all()
	return render(request, 'scheduling_interview/list.html', {'list1':queryset})


def edit_interview(request, id):
    post = get_object_or_404(InterviewCreation, interview_id=id)
    if request.method == "POST":
        form = EditForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            int_id=InterviewCreation.objects.get(interview_id=id)
            old_interviewer_email= Interviewer.objects.get(interview_id= int_id)
            old_interviewer_email.delete()
            old_candidate_email=Interviewee.objects.get(interview_id=int_id)
            old_candidate_email.delete()
            interviewee_email=form.cleaned_data['interviewee_email']
            interviewer_email=form.cleaned_data['interviewer_email']           
            I=Interviewer(email=interviewer_email,interview_id=int_id)
            I.save()
            C=Interviewee(email=interviewee_email,interview_id=int_id)
            C.save()
            return HttpResponse("successfully_edited")
    else:
        form = EditForm(instance=post)
    return render(request, 'scheduling_interview/create.html', {'form': form})

                

        







	







