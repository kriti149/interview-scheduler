from django import forms
from .models import *
from django.core.exceptions import ValidationError
import urllib.request
import json
#import requests

class DetailsForm(forms.Form):
	interview_id=forms.CharField(label='Please enter interview id')	
	interviewee_email=forms.EmailField(label='Please enter email id of candidate')
	interviewer_email=forms.EmailField(label='Please enter email id of interviewer')	
	start_time=forms.TimeField(label='Enter interview start time')
	end_time=forms.TimeField(label='Enter interview end time')

class EditForm(forms.ModelForm):
	class Meta:
		model=InterviewCreation
		fields=['interview_id','interviewee_email','interviewer_email','start_time','end_time']
	
	






