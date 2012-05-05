from cup_oj.problem.views import *
from django.conf.urls import patterns, url

urlpatterns = patterns('',    
    url(r'^compilable_code_generation_config_upload/$', compilable_code_generation_config_upload, name='compilable_code_generation_config_upload'),
    url(r'^compile_config_upload/$', compile_config_upload, name='compile_config_upload'),
    url(r'^input_output_data_upload/$', input_output_data_upload, name='input_output_data_upload'),
    url(r'^keyword_checkconfig_upload/$', keyword_checkconfig_upload, name='keyword_checkconfig_upload'),
    url(r'^output_check_config_upload/$', output_check_config_upload, name='output_check_config_upload'),
    url(r'^problem_meta_upload/$', problem_meta_upload, name='problem_meta_upload'),                 
    url(r'^submit_success/$', submit_success, name = 'submit_success'),
    
)
