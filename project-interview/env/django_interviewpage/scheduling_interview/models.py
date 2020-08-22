from django.db import models

# Create your models here.
class User_Detail(models.Model):
	name=models.CharField(max_length=20,default="")
	email=models.EmailField(default="")
	phone=models.IntegerField(default=0)
	address=models.TextField(default="")
	
	def __str__(self):
		return self.email


class InterviewCreation(models.Model):
	interview_id=models.CharField(max_length=20,default="")
	interviewee_email=models.EmailField(default="")	
	interviewer_email=models.EmailField(default="")	
	start_time=models.TimeField(auto_now=False, auto_now_add=False)
	end_time=models.TimeField(auto_now=False, auto_now_add=False)
		
	def __str__(self):
		return self.interview_id

class Interviewer(models.Model):	
	email=models.EmailField(default="")
	interview_id=models.ForeignKey(InterviewCreation,on_delete=models.CASCADE)
		
	def __str__(self):
		return self.email


class Interviewee(models.Model):	
	email=models.EmailField(default="")
	interview_id=models.ForeignKey(InterviewCreation,on_delete=models.CASCADE)
		
	def __str__(self):
		return self.email
		
