# interview-scheduler
It is a simple app where we can create interviews by entering participant emails (for interviewer and the candidate), interview start time and end time.

Description of MVT(Model,View,Template):

MODEL-
There are 4 classes(4 relations or tables).

1)User_Detail- It contains all the information about the users i.e. their name, email-id, phone number and address(Users are created directly in this relation).
2)InterviewCreation- It contains all the information needed to schedule interviews i.e. email ids of both the interviewer and the candidate, start and end time of the interview and most importantly the interview-id(needed to distinguish different interviews,i.e.primary key).
3)Interviewer- It contains the email-ids of the interviewers of the interviews alongwith the interview-ids.
4)Interviewee- It contains the email-ids of the candidates of the interviews alongwith the interview-ids.

VIEW-
There are 3 different views needed to create, edit and list the interview details.

1)create_interview_page- It takes the data(interview_id,start_time,end_time,candidate_email,interviewer_email) from the admin(person who would create the interview) using "forms" 
and stores the data in the database(InterviewCreation,Interviewer,Interviewee). Once the data is successfully saved in the database it would return the HTTPResponse saying that data is successfully saved. If the admin tries to enter the email-ids(candidate or interviewer) which are not in the relation User_Detail it would throw error and return response saying the ids not in database. Also if the admin tries to schedule the interview and if either interviewer or candidate is busy in another interview that time then it would throw error and return response saying that candidate or interviewer is busy.

2)list_interview_details- It would simply print the details of all the interviews(interview_id,start_time,end_time,candidate_email,interviewer_email) in the tabular format.

3)edit_interview- It would first display the details of the interview and then the admin the edit the details in the form and the changes would be saved in the database(InterviewCreation,Interviewer,Interviewee).

TEMPLATE-
There are 2 templates used.

1)create.html- It is used to create the form to ask the admin to enter the details of the interview. It is used by create_interview_page view.
2)list.html- This template would get the data from the list_interview_details view to display the interview details.


