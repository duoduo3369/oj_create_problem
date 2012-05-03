from cup_oj.problem.views import *
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^problem_meta/$', problem_meta_upload, name='problem_meta_upload'),                 
    
)
