from cup_oj.problem.views import *
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^problem_meta_upload/$', problem_meta_upload, name='problem_meta_upload'), 
    url(r'^keyword_checkconfig_upload/$', keyword_checkconfig_upload, name='keyword_checkconfig_upload'),                
    url(r'^submit_success/$', submit_success, name = 'submit_success'),
)
