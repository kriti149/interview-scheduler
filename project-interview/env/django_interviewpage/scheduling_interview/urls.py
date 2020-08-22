from django.conf.urls import url, include
from django.views.generic import ListView, DetailView

from .views import *


urlpatterns= [url('^create/', create_interview_page),url('list/', list_interview_details),
url(r'^(?P<id>\d+)/edit/', edit_interview),]
